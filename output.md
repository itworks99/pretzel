## Release

A release pipeline definition consisting of phases to release to production.

| Property        | Type                  | Description                         | Required |
| :-------------- | :-------------------- | :---------------------------------- | :------- |
| **Name**        | `string`              | Name of the release pipeline.       | `Yes`    |
| **Description** | `string`              | Summary of the release pipeline.    |          |
| **Phases**      | [`Phase`](#Phase)`[]` | The phases of the release pipeline.</br>E.g. `DEV`, `TEST` or `PROD`. | `Yes`    |

---

## Phase

An individual phase of a release pipeline. Can be tied to environments such as `DEV`, `TEST` or `PROD`. Names of phases are representative of what they do.

| Property        | Type       | Description                                   | Required |
| :-------------- | :--------- | :-------------------------------------------- | :------- |
| **Name**        | `string`   | Name of the deployment pipeline phase.        | `Yes`    |
| **Description** | `string`   | Description of the phase.                     |          |
| **Actions**     | `string[]` | List of actions to be performed in the phase. |          |
