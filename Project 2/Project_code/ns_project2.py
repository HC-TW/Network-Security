import sys
import pandas as pd
import os
from os import listdir
from os.path import join

def check_Port_Scan(beat_file, attack_score, file):
    if file == 'packetbeat.json':
        visited_ports = []
        for index, row in beat_file.iterrows():
            if 'event' in row.keys():
                event = row['event']
                if 'duration' in event.keys():
                    if event['duration'] == 0:
                        if 'destination' in row.keys():
                            destination = row['destination']
                            if 'port' in destination.keys() and 'packets' in destination.keys() and 'bytes' in destination.keys():
                                if destination['port'] not in visited_ports and destination['packets'] == 1 and destination['bytes'] < 100:
                                    attack_score[0] += 1
                                    visited_ports.append(destination['port'])

def check_SQL_Injection(beat_file, attack_score, file):
    if file == 'packetbeat.json':
        if 'url' in beat_file.keys():
            for url in beat_file['url']:
                if not pd.isnull(url):
                    if 'query' in url.keys():
                        if 'UNION' in url['query'] or 'SELECT' in url['query'] or 'INSERT' in url['query'] or \
                            'DELETE' in url['query'] or 'UPDATE' in url['query'] or 'WHEN' in url['query'] or \
                            'EXISTS' in url['query'] or 'FROM' in url['query'] or 'THEN' in url['query'] or \
                            'ELSE' in url['query'] or 'END' in url['query']:
                                attack_score[1] += 1

def check_Brute_Force(beat_file, attack_score, file):
    if file == 'packetbeat.json':
        brute_username = []
        if 'url' in beat_file.keys():
            for url in beat_file['url']:
                if not pd.isnull(url):
                    if 'query' in url.keys():
                        if 'username' in url['query'] and 'password' in url['query']:
                            split_vector = url['query'].split('&')
                            for s in split_vector:
                                if 'username' in s:
                                    username = s[9:]
                                    if username in brute_username:
                                        attack_score[2] += 1
                                    else:
                                        brute_username.append(username)

def check_DDoS(beat_file, attack_score, file, DDoS_winlog_process_pid):
    if file == 'winlogbeat.json':
        pid_count = 0
        pid_4_count = 0
        if 'winlog' in beat_file.keys():
            for winlog in beat_file['winlog']:
                if not pd.isnull(winlog):
                    if 'process' in winlog.keys():
                        winlog_process = winlog['process']
                        if 'pid' in winlog_process.keys():
                            pid_count += 1
                            if winlog_process['pid'] == 4:
                                pid_4_count += 1
        if pid_count > 0:
            if pid_4_count / pid_count > 0.9:
                return True

    elif file == 'packetbeat.json':
        if 'destination' in beat_file.keys():
            for destination in beat_file['destination']:
                if not pd.isnull(destination):
                    if 'port' in destination.keys() and 'packets' in destination.keys():
                        if destination['port'] == 80 and destination['packets'] > 10:
                            attack_score[3] += 1

    return DDoS_winlog_process_pid

def check_Phishing_Email(beat_file, attack_score, file):
    if file == 'winlogbeat.json':
        if 'winlog' in beat_file.keys():
            for winlog in beat_file['winlog']:
                if not pd.isnull(winlog):
                    if 'event_data' in winlog.keys():
                        winlog_event_data = winlog['event_data']
                        if 'Application' in winlog_event_data.keys():
                            if 'svchost.exe' in winlog_event_data['Application']:
                                attack_score[4] += 1

def determine_attack_train(attack_score, dir):
    max_index = 0
    max_value = attack_score[0]
    for i in range(1, 5):
        if attack_score[i] > max_value:
            max_value = attack_score[i]
            max_index = i
    attack_dict[attack_types[max_index]] = 'attack ' + dir[-1]

def determine_attack_test(attack_score, dir):
    max_index = 0
    max_value = attack_score[0]
    for i in range(1, 5):
        if attack_score[i] > max_value:
            max_value = attack_score[i]
            max_index = i
    testcase_attack_output['testcase ' + dir[-1]] = attack_dict[attack_types[max_index]]

def load(path):
    (_, dirs, _) = next(os.walk(path))
    for dir in dirs:
        #print(dir)
        attack_score = [0]*5
        DDoS_winlog_process_pid = False
        for file in listdir(join(path, dir)):
            beat_file = pd.read_json(join(path, dir, file), lines=True)
            beat_file.head()
            # calculate attack score
            check_Port_Scan(beat_file, attack_score, file)
            check_SQL_Injection(beat_file, attack_score, file)
            DDoS_winlog_process_pid = check_DDoS(beat_file, attack_score, file, DDoS_winlog_process_pid)
            check_Brute_Force(beat_file, attack_score, file)
            check_Phishing_Email(beat_file, attack_score, file)

        if not DDoS_winlog_process_pid:
            attack_score[3] = 0
        
        # determine attack type
        if path == './Logs/Train':
            determine_attack_train(attack_score, dir)
        else:
            determine_attack_test(attack_score, dir)
    
        """ print('Port Scan score: ', attack_score[0])
        print('SQL Injection Score: ', attack_score[1])
        print('Brute Force score: ', attack_score[2])
        print('DDoS score: ', attack_score[3])
        print('Phishing Email score: ', attack_score[4]) """
    return len(dirs)

def main():
    # training data
    #load(training_data_path)
    #print(attack_dict)

    # tesing data 
    testcase_count = load(testing_data_path)
    for i in range(1, testcase_count+1):
        print('testcase', str(i) + ':' , testcase_attack_output['testcase ' + str(i)])

training_data_path = './Logs/Train'
testing_data_path = sys.argv[1]
attack_types = ['Port Scan', 'SQL Injection', 'Brute-Force attack', 'DDoS', 'Phishing Email']
attack_dict = {'Port Scan': 'attack 3', 'SQL Injection': 'attack 5', 'Brute-Force attack': 'attack 1', 'DDoS': 'attack 2', 'Phishing Email': 'attack 4'}
testcase_attack_output = {}

if __name__ == "__main__":
    main()