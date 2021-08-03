# Network-Security
## Project 1
### Project Description
The goal of this project is to introduce you to logs and ELK Stack environment. ELK Stack is an
platform used to collect and analyze logs. By the end of this semester, you should be more familiar with
logs and ELK Stack environment. In this project, you’ll practice how to set up and use ELK to observe
and analyze the logs.
### Project Guide
1. **Environment:** Use Ubuntu Server 18.04LTS 64bit and Windows 10 operating system for this
project. Ubuntu is for setting up ELK environment and Windows is using to reproduce logs of the
scenarios and upload it to your Logstash. You can use your own computers or install new VMs, yet
setting up a new VM is recommended since the logs will be fewer and easier to observe later. (You
can find Ubuntu image at https://www.ubuntu-tw.org/modules/tinyd0/ and Windows 10 image at
university’s FTP server : ca.nctu.edu.tw.)\
The minimum hardware requirements for Ubuntu,
    - Memory 4G (Recommend 8G for better fluency)  
    - Hard disk 40G
    - Swap space 4G
2. **Tools you need to install:**
    1. Ubuntu
        1. Docker:\
            Docker is a tool which provides the way to create, manage, and deliver container applications.
        2. ELK Stack:\
            ”ELK” is the acronym for three open source projects: Elasticsearch, Logstash, and
            Kibana, and it is used to collect, search, analyze logs. We will provide the docker files for
            you to set up your ELK stack more easily. The link of the files is
            https://drive.google.com/uc?id=1i8dsqoEe226EjuxkSKnzOh8Xc5Hmt-b&export=download
    2. Windows
        1. Winlogbeat:
            Winlogbeat is a Windows specific event-log shipping agent installed as Windows service. It
            can be used to collect and send event logs to one or more destinations, including Logstash.
            https://www.elastic.co/downloads/beats/winlogbeat
        2. Packetbeat:
            Packetbeat is lightweight network packet analyzer that sends data from your hosts and
            containers to Logstash or Elasticsearch. https://www.elastic.co/beats/packetbeat
3. **Implement events and observe:** For this part, you are asked to reproduce 5 of the following
scenarios and find the corresponding logs on ELK. Everyone’s set of events is different, find your
set in NS project1 sets.xlsx which has been uploaded on the new e3 platform. Scenarios:
    1. Logon Success:\
        Sign in to your computer with your account name and password.
    2. Logoff:\
        Sign out.
    3. Screensaver invoked:\
        Turn on screen saver setting and invoke a screen saver.
    4. Screensaver dismissed:\
        Dismiss a screen saver.
    5. Open the specific application:\
        Open the calculator.exe.
    6. Close the specific application:\
        Close the calculator.exe.
    7. Create file:\
        Create a new file.
    8. Change file name:\
        Change a existed file’s name.
    9. DNS query:\
        You may use nslookup command to create the log. The domain is required to be youtube.com.
    10. Visit http website:\
        The website is require to be http://www.fybus.com.tw/
## Project 2
### Project Description
The goal of this project is to practice cyber attack log analysis. This is a personal project, each of
you will be provided with 5 sets of data collected when different attacks are carried out. You have to
implement a classifier to classify different attack scenarios. You can either observe the logs and then
write a **rule-based model** or use **machine learning method** to tune a best-result model. You are
encouraged to use ELK stack in project1 to perform the analysis.
### Project Guide
1. **Project Target:**
The goal of this project is to practice analyzing logs. Log can be analyzed in many different ways
for different purposes, and for this project, you are practicing classifying attack type with simple
attack cases. In this project, you need to first observe the logs, then pre-process the logs, and then
finally construct a classification model.
2. **Keywords:**
    1. Log Analysis:\
        Log analysis is the process of making sense of computer-generated log messages, also known
        as log events, audit trail records, or simply logs. Log analysis provides useful metrics that
        paint a clear picture of what has happened across the infrastructure. You can use this data to
        improve or solve performance issues within an application or infrastructure. Looking at the
        bigger picture, companies analyze logs to proactively and reactively mitigate risks, comply
        with security policies, audits, and regulations, and understand online user behavior.
    2. Machine Learning:\
        Machine learning (ML) is the study of computer algorithms that improve automatically
        through experience. It is seen as a subset of artificial intelligence. Machine learning algorithms build a mathematical model based on sample data, known as         ”training data”, in order
        to make predictions or decisions without being explicitly programmed to do so. Machine
        learning algorithms are used in a wide variety of applications, such as email filtering and computer vision, where it is difficult or infeasible to develop         conventional algorithms to perform
        the needed tasks.
    3. Cyber Attack:\
        In computers and computer networks an attack is any attempt to expose, alter, disable,
        destroy, steal or gain unauthorized access to or make unauthorized use of an asset.[1] A
        cyberattack is any type of offensive maneuver that targets computer information systems,
        infrastructures, computer networks, or personal computer devices. An attacker is a person or
        process that attempts to access data, functions or other restricted areas of the system without
        authorization, potentially with malicious intent.
### Attack Scenarios
- **Attack Scenario Description:**
    - **Port Scan:**\
        The logs are collected from a host that was attacked by port scan.
        A port scan is an attack that sends client requests to a range of server port addresses on
        a host, with the goal of finding an active port and exploiting a known vulnerability of that
        service. Scanning, as a method for discovering exploitable communication channels, has been
        around for ages.
    - **SQL Injection:**\
        The logs are collected from a web server that has a SQL database vulnerability and was attacked by SQL injection.
        SQL injection is a code injection technique, used to attack data-driven applications, in which
        malicious SQL statements are inserted into an entry field for execution (e.g. to dump the
        database contents to the attacker). For example, when user input is either incorrectly filtered
        for string literal escape characters embedded in SQL statements or user input is not strongly
        typed and unexpectedly executed.
    - **Brute-Force attack:**\
        The logs are collected from a web server that was attacked by brute-force attack. The attacker
        attempted to guess the username and password.
        A brute-force attack consists of an attacker submitting many passwords or passphrases with
        the hope of eventually guessing correctly.
    - **DDoS:**\
        The logs are collected from a web server that was attacked by Dos. In other words, the web
        service was overwhelmed by numerous requests. The web service is running on the default
        port 80.
        Denial of service(Dos) is typically accomplished by flooding the targeted machine or resource
        with superfluous requests in an attempt to overload systems and prevent some or all legitimate
        requests from being fulfilled.
    - **Phishing Email(Malicious Attachment):**\
        The log is collected by a host that accidentally downloaded a malicious pdf attachment from an
        email. The attacker used the pdf file to attack the Adobe acrobat vulnerability and managed
        to exploit the CVE. After obtaining control of cmd.exe, the attacker searched for the desired
        data. Finally, compressed the data with tar and transferred to their own server.
