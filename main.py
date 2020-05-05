import pandas as pd
import numpy as np
from validate_utf8 import find_utf8_errors
import os
import glob
from collections import namedtuple
import json
import jsonschema


COVID_19_REPO_FOLDER = 'COVID-19'
if not os.path.exists(COVID_19_REPO_FOLDER):
    COVID_19_REPO_FOLDER = '../' + COVID_19_REPO_FOLDER + '.git'
    if not os.path.exists(COVID_19_REPO_FOLDER):
        raise Exception('Could not find "{0}" folder'.format(COVID_19_REPO_FOLDER))

SCHEMAS_FOLDER = 'schemas'


ErrorEntry = namedtuple("ErrorEntry", ("filename", "errors"))

schemas = {}
def getJsonSchemaFor(filename):
    basename = os.path.basename(filename)
    schemaName, ext = os.path.splitext(basename)
    suffix = '-latest'
    if schemaName.endswith(suffix): schemaName = schemaName[:-len(suffix)]
    schemaName = os.path.join(SCHEMAS_FOLDER, schemaName + '.schema')
    #print(schemaName)
    if schemaName in schemas:
        schema = schemas[schemaName]
    else:
        if not os.path.exists(schemaName):
            raise Exception('No schema file named "{0}".'.format(schemaName))
        with open(schemaName, 'r') as jsonFile:
            schema = json.load(jsonFile)
            schemas[schemaName] = schema
            print('[LOAD SCHEMA] {0}'.format(os.path.basename(schemaName)))

    return schema


if __name__ == '__main__':
    print('Hello Github Action Python')

    print('[COVID FOLDER] {0}'.format(COVID_19_REPO_FOLDER))

    print()

    csvFiles = glob.glob(COVID_19_REPO_FOLDER + '/*/*.csv')
    jsonFiles = glob.glob(COVID_19_REPO_FOLDER + '/*/*.json')

    errorsList = []

    filesToValidate = csvFiles + jsonFiles
    print('[UTF8] Validating utf8 in {0} files...'.format(len(filesToValidate)))
    for file in filesToValidate:
        with open(file, 'rb') as f:
            fileContent = f.read()
            errors = find_utf8_errors(fileContent)
            if errors:
                errorsList.append(ErrorEntry(file, errors))

    print('- Errors found: {0}'.format(len(errorsList)))
    for i, entry in enumerate(errorsList):
        print('  [{0:02}] {1}'.format(i, entry.filename))
        for error in entry.errors:
            print('     ' + error.extract)
        print()


    verboseJsonErrors = True
    errorsList = []

    print('[JSON] Validating json schema in {0} files...'.format(len(jsonFiles)))
    for file in jsonFiles:
        schema = getJsonSchemaFor(file)
        #print(file)
        #print(file, schema)
        with open(file, 'r') as f:
            instance = json.load(f)
            try:
                jsonschema.validate(instance=instance, schema=schema, format_checker=jsonschema.FormatChecker())
            except jsonschema.exceptions.ValidationError as e:
                errorsList.append(ErrorEntry(file, e))

    print('- Errors found: {0}'.format(len(errorsList)))
    for i, entry in enumerate(errorsList):
        print('  [{0:02}] {1}'.format(i, entry.filename))
        if not verboseJsonErrors:
            print('       ' + entry.errors.message)
        else:
            error = str(entry.errors)
            error = error.replace('\n', '\n       ')
            print('       ' + error)
        print()
