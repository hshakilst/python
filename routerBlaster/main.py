import urllib2
import urllib

def main():
    userName = 'admin'
    pcPassword = 'admin'
    login_data = urllib.urlencode({'userName': userName, 'pcPassword': pcPassword})
    r = urllib2.Request('http://192.168.0.1/userRpm/LoginRpm.htm')
    r.add_header("Content-Type", "application/x-www-form-urlencoded")
    r.add_header("Content-Length", str(len(login_data)))
    r.add_data(login_data)
    u = urllib2.urlopen(r)
    print u.read()
    u.close()
if __name__ == '__main__':
    main()