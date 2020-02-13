import json
import os
import sys

import click

md = ''

table_header = ''
table_header += '| Property        | Type                  | Description                         | Required |\n'
table_header += '| :-------------- | :-------------------- | :---------------------------------- | :------- |\n'

md_section_break = '\n' + '---' + '\n'

index = 0
parent = 0
imported_records = []


@click.command()
@click.option('-f', '--json-file', 'jsonfile', required=True, type=str)
def pretzel(jsonfile):

    global md
    global table_header
    global md_section_break
    global imported_records

    try:
        file = open(jsonfile)
        if file:
            json_file = file.read()
            file.close()
            json_src = json.loads(json_file)

            iterate_over_json_dictionary(json_src)

            title = ''
            type_ = ''
            desc = ''
            required = ''
            required_yes = ''

            for record in imported_records:
                if record[2] == "title":
                    title = record[3]
                if record[2] == "type":
                    type_ = record[3]
                if record[2] == "description":
                    desc = record[3]
                if record[2] == "required":
                    required = record[3]

                if title != "" and type_ != "" and desc != "":

                    if required:
                        required_yes = lookup_required_fields(title, required)

                    if type_ != 'object':
                        if type_ == 'array':

                            array_name = lookup_array_name(
                                type_, imported_records.index(record))

                            md += '|**' + title + '**|' + array_name + \
                                "|" + desc + "|" + required_yes + "|\n"
                        else:
                            md += '|**' + title + "**|`" + type_ + "`|" + desc + "|" + required_yes + "|\n"

                    elif type_ == 'object':
                        md += md_section_break
                        md += markdown_header(title)
                        md += markdown_header_description(desc)
                        md += table_header

                    title = ''
                    type_ = ''
                    desc = ''
                    required_yes = ''
        print(md)

    except OSError as err:
        print("Configuration file not found!")
        print("OS error: {0}".format(err))
        raise


def iterate_over_json_dictionary(dictionary):

    global index
    global parent
    index += 1
    global imported_records
    for key, value in dictionary.items():
        if (isinstance(value, dict)):
            parent = index
            iterate_over_json_dictionary(value)
        else:
            imported_records.append([index, parent, key, value])


def lookup_array_name(title, index):
    global imported_records
    array_name = ''
    if (imported_records[index + 1])[2] == 'title':
        array_name = (imported_records[index + 1][3])
        return ("[`" + array_name + '`](#' + array_name + ')`[]`')
    else:
        return("`String[]`")


def lookup_required_fields(title, required):
    if title.lower() in required:
        return "`YES`"
    else:
        return ""


def markdown_header(input):
    return('## ' + input + '\n\n')


def markdown_header_description(input):
    return (input + '\n\n')


pretzel()
