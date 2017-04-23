from neo4j.v1 import GraphDatabase, basic_auth
from neo4j.exceptions import ServiceUnavailable, ClientError, AuthError, SecurityError
from time import sleep
import sys

secondsToSleep = 10

for i in range(5,0,-1):
    try:
        driver = GraphDatabase.driver("bolt://neo4j:7687", auth=basic_auth("neo4j", "12345"))
        session = driver.session()
    except (ServiceUnavailable, ClientError, AuthError, SecurityError) as e:
        if i == 1:
            raise
        sleep(secondsToSleep)
        print('retry %d after catching %s; sleeping for %d seconds' % (i,str(e), secondsToSleep))
    else:
        break    
        
result = session.run('MERGE (f:Person {name:"Frederik Durant", yob:1968}) ON CREATE SET f.created = timestamp()')
result = session.run("MATCH (a:Person) RETURN count(a) as numberOfActors")

for record in result:
    print >> sys.stderr, record
