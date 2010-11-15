from suds.client import Client

if __name__ == '__main__':
    client = Client('http://localhost:7789/?wsdl')
    sd =  client.service.getServiceDescription(None, [])
    print sd.requiresRegistration
