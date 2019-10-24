#!/usr/bin/env python

from jsonschema import validate

schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",

    "definitions": {
        "body": {
            "type": "array",
            "items": {
                "anyOf": [
                    {"type": "object", "properties": {"name": {"type": "string"}}},
                    {"type": "object", "properties": {"test": {"type": "string"}}}
                    #"test": {"$ref": "#/definitions/body"},
                ]
            }
        }
    },

    "type": "object",
    "properties": {
        "document": {"body": {"$ref": "#/definitions/body"}}
    }
}

doc = {
    "document": {
        "body": [
            {"name": 1},
            {"test": []}
        ]
    }
}

validate(instance=doc, schema=schema)
