import json
import os
import sys

import click
import numpy as np

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
    header = ""

    try:
        file = open(jsonfile)
        if file:
            json_file = file.read()
            file.close()
            json_src = json.loads(json_file)

            iterate_over_json_dictionary(json_src)

            print(imported_records)
            index = 0
            title = ''
            type_ = ''
            desc = ''
            required = ''
            for record in imported_records:
                index = record[0]
                if record[2] == "title":
                    title = record[3]
                if record[2] == "type":
                    type_ = record[3]
                if record[2] == "description":
                    desc = record[3]
                if record[2] == "required":
                    required = str(record[3])

                if title != "" and type_ != "" and desc != "":
                    if type_ != 'object':
                        if type_ == 'array':
                            md += '|**' + title + '**|' + \
                                "[`" + title + '`](#' + title + ')`[]`' + \
                                "|" + desc + "|" + required + "|\n"
                        else:
                            md += '|**' + title + '**|' + type_ + "|" + desc + "|" + required + "|\n"

                    elif type_ == 'object':
                        md += md_section_break
                        md += markdown_header(title)
                        md += markdown_header_description(desc)
                        md += table_header
                    title = ''
                    type_ = ''
                    desc = ''
                    required = ''
        print(md)

    except OSError as err:
        print("Configuration file not found!")
        print("OS error: {0}".format(err))
        raise


def iterate_over_json_dictionary(d):

    global index
    global parent
    index += 1
    global imported_records
    for k, v in d.items():
        if (isinstance(v, dict)):
            parent = index
            iterate_over_json_dictionary(v)
        else:
            imported_records.append([index, parent, k, v])


def markdown_header(input):
    return('## ' + input + '\n\n')


def markdown_header_description(input):
    return (input + '\n\n')


def traverse_json_object(json_src):
    md_output_line = ''
    md = ''
    for field in json_src:
        title = ''
        type_ = ''
        desc = ''
        required = ''

        for item in json_src[field]:

            if item == "title":
                title = str(json_src[field][item])

            if item == "type":
                type_ = str(json_src[field][item])

            if item == "description":
                desc = str(json_src[field][item])

            if item == 'required':
                required = "` Yes `"

        if type_ == 'array':
            md_output_line += '|**' + title + '**|' + \
                "[`" + title + '`](#' + title + ')`[]`' + \
                "|" + desc + "|" + required + "|\n"
        else:
            md_output_line += '|**' + title + '**|' + \
                type_ + "|" + desc + "|" + required + "|\n"

        md += md_output_line
        md_output_line = ''

    return md


pretzel()
