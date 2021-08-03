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
