# SCAM AND_PHISHING_SITE_DETECTOR
Is a Malicious URL Scanner that returns many data points 
so your business logic can make the best decisions. Analyzing the 
overall Risk Score is usually the best way to determine domain 
reputation and the overall scoring confidence level. It scans 
links in real-time to detect suspicious URLs. Accurately identify 
phishing links, malware URLs and viruses, parked domains, and suspicious URLs with real-time risk scores. Industry leading phishing detection and domain reputation provide better signals for more accurate decision making. 
The script utileses API from www.ipqualityscore.com.

    Used for detecting: Scanner Use Cases
* Phishing URL Detection — Detect malicious URLs used for phishing campaigns and misleading advertising.
* Malicious URL Scanning — Identify URLs used for malware and viruses with live threat intelligence feeds that detect zero-day phishing links and suspicious behavior.
* Parked Domain Detection — Detect parked domains and easily classify parked domains via API such as ParkingCrew, Sedo, Bodis, Skenzo, ParkLogic, Rook Media, Voodoo, and recognition for all types of parked domains.
* Abusive Domains - Block emails from disposable email services and throwaway accounts. Pair with IP reputation checks for deeper insight.


# SCAN RESULT MEANING
    unsafe ------- Is a malicious domain  --------- boolean string
    ip_address --- The IP of the domain name -----  string
    risk_score --- the confidence level for malicious URL detection. Risk Scores 85+ are high risk, while Risk Scores = 100 are confirmed as accurate. integer, 0 - 100
    status_code -- HTTP Status Code of the URL's response. This value should be "200" for a valid website. Value is "0" if URL is unreachable.
    domain_rank -- Estimated popularity rank of website globally. Value is "0" if the domain is unranked or has low traffic.
    suspicious --- Is this URL suspected of being malicious or used for phishing or abuse? Use in conjunction with the "risk_score" as a confidence level.
    phishing ----- Is this URL associated with malicious phishing behavior?
    malware ------ Is this URL associated with malware or viruses?
    parking ------ Is the domain of this URL currently parked with a for sale notice?
    spamming ----- Is the domain of this URL associated with email SPAM or abusive email addresses?
    adult -------- Is this URL or domain hosting dating or adult content?
    category ----- Website classification and category related to the content and industry of the site. Over 70 categories are available including "Video Streaming", "Trackers", "Gaming", "Privacy", "Advertising", "Hacking", "Malicious", "Phishing", etc. The value will be "N/A" if unknown.
    domain_age --- How long the website name has been up in terms of days-to-years

# Scan result sample

    |"message": "Success.", | "success": true, |

    |"unsafe": false, | "domain": "google.com",|	

    |"ipAddress":"10.10.7.",| "domain_rank": 1,|

	|"dns_valid": true, | "parking": false,|
    
    |"spamming": false, | "malware": false,|

	|"phishing": false, | "suspicious": false,|

	|"adult": false, | "risk_score": 0,|

	|"domain_age": {"human": "3 months ago",|


# REQUIREMENTS
* LINUX OS
* Windows
* Python 
* git (optional, for easy cloning of repo/download)


    
    More updates for easy accessibility and wider device coverage will be rolled out.

    Installation/Usage:
    from terminal run:

Run the updates 
    
    sudo apt-get update | not needed on windows
    sudo apt-get upgrade| not needed on windows

Install git

    apt-get install git | windows download: https://central.github.com/deployments/desktop/desktop/latest/win32?format=msi

install the scanner


    git clone https://github.com/CybSec-LAB/Scam_and_phishing_site_detector | do same for windows of download the files from github: https://github.com/CybSec-LAB/Scam_and_phishing_site_detector

Extract the tool


    unzip Scam_and_phishing_site_detector | extract using winrar or zip

Navigate to the tool directory

    cd /home/user/folder/Scam_and_phishing_site_detector | window users have to run in terminal or python IDE

Run the tool

    python scam_and_phishing_url_scanner.py | window users have to run in terminal or python IDE


    Enter/paste the URL to scan
    Results will be displayed in the terminal