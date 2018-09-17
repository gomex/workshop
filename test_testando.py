def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_hosts_socket(host):
 s = host.socket("tcp://0.0.0.0:8080")
 
 assert s.is_listening
