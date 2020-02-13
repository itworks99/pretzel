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


@click.command()
@click.option('-f', '--json-file', 'jsonfile', required=True, type=str)
def pretzel(jsonfile):

    global md
    global table_header
    global md_section_break
    header = ""

    try:
        file = open(jsonfile)
        if file:
            json_file = file.read()
            file.close()
            json_src = json.loads(json_file)

            md += markdown_header(json_src["title"])
            md += markdown_header_description(json_src["description"])

            json_src = json_src["properties"]

            md += table_header

            md += traverse_json_object(json_src)

            md += md_section_break

            for section in json_src:
                md += '\n\n'
                for entry in json_src[section]:
                    object = json_src[section][entry]
                    if type(object) is not dict:
                        if header == "":
                            header += markdown_header(
                                json_src[section]['title'])
                            header += markdown_header_description(
                                json_src[section]['description'])
                    else:
                        md += header
                        md += table_header
                        md += traverse_json_object(object)
            print(md)

    except OSError as err:
        print("Configuration file not found!")
        print("OS error: {0}".format(err))
        raise


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

        if md_output_line != '|||||':
            md += md_output_line
        md_output_line = ''

    print(json_src.keys())

    return md


pretzel()
