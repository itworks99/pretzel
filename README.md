# 🥨 pretzel

JSON schema to markdown converter. To run:

    python3 pretzel.py -f input.json > output.md

## Example

JSON schema:

```json
{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Release",
    "description": "A pipeline definition consisting of phases to release to production.",
    "type": "object",
    "required": [
        "name",
        "phases"
    ],
    "properties": {
        "name": {
            "title": "Name",
            "description": "Name of the release pipeline.",
            "type": "string"
        },
        "description": {
            "title": "Description",
            "description": "Description of the release pipeline.",
            "type": "string"
        },
        "phases": {
            "title": "Phases",
            "description": "The phases of the release pipeline.",
            "type": "array",
            "items": {
                "title": "Phase",
                "type": "object",
                "description": "An individual phase of a release pipeline. Can be tied to environments such as `DEV`, `TEST` or `PROD`. Names of phases are representative of what they do.",
                "required": [
                    "name"
                ],
                "properties": {
                    "name": {
                        "title": "Name",
                        "description": "Name of the deployment pipeline phase",
                        "type": "string"
                    },
                    "description": {
                        "title": "Description",
                        "description": "Description of the phase",
                        "type": "string"
                    },
                    "actions": {
                        "title": "Actions",
                        "description": "Actions to be performed in the phase",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                }
            }
        }
    }
}
```

same schema after being converted to markdown:

---
## Release

A pipeline definition consisting of phases to release to production.

| Property        | Type                  | Description                          | Required |
| :-------------- | :-------------------- | :----------------------------------- | :------- |
| **Name**        | `string`              | Name of the release pipeline.        | `YES`    |
| **Description** | `string`              | Description of the release pipeline. |          |
| **Phases**      | [`Phase`](#Phase)`[]` | The phases of the release pipeline.  | `YES`    |

---
## Phase

An individual phase of a release pipeline. Can be tied to environments such as `DEV`, `TEST` or `PROD`. Names of phases are representative of what they do.

| Property        | Type       | Description                           | Required |
| :-------------- | :--------- | :------------------------------------ | :------- |
| **Name**        | `string`   | Name of the deployment pipeline phase | `YES`    |
| **Description** | `string`   | Description of the phase              |          |
| **Actions**     | `String[]` | Actions to be performed in the phase  |          |