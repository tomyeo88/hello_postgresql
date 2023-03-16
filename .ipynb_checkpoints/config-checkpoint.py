from configparser import ConfigParser
import os

def test_connection(filename='config_db.ini', section='postgresql'):
    # get full path to the config file
    filepath = os.path.join('/Users/minguyeo/Documents/coding/pythonPJT/config',filename)
    # create a parser
    parser = ConfigParser()
    # read file
    parser.read(filepath)
    
    #get section, default (psql)
    db={}
    # check to see if section(psql) parser exists
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
            
    # return an error if param is called that is NOT listed in (init) file
    
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db
