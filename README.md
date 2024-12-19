# Dean's Crisis Management System


# Setup envirment

## On *nix

1. Install `docker` and `docker-compose` correctly.

[How to install on mac](http://sourabhbajaj.com/mac-setup/Docker/)

2. Setup python
```shell
$ virtualenv -p python3 env 
$ source env/bin/activate
$ pip install -r requirments.txt
```

## On Windows
```
```

# Run server

If on Mac or Windows the container will run on Docker Machine which is a virtual machine, and will have its own ip address. You could run`docker-machine ip` to check the address, and such address will used to access the front end. However, on Linux, you could simplly access `localhost`.

## On *nux

If using you will need `sudo` to run the following command.
```shell
$ docker-compose up
```

## On Windows

```

```


# Useful commands

## Django migrattion

``` shell
docker-compose run web python manage.py migrate
```

# TODO

- [ ] persist data in a dockerized postgres database using volumes
- [ ] django-restful doc
- [ ] remove 'ADD' on setting page
- [ ] 


# Appendix A: Checklist

## Intention-Based Classification Software Maintenance

| Type                        | Implementation Status | Person in Charge           | Justification                                                                                           |
|-----------------------------|-----------------------|----------------------------|-------------------------------------------------------------------------------------------------------|
| Corrective Maintenance      | ✓                     | Koo Song Le                | The program can not run in the current state without finding the correct dependencies.               |
| Adaptive Maintenance        | ✓                     | Koo Song Le                | Some dependencies have higher stable versions that may be used.                                      |
| Perfective Maintenance      | ✓                     | Abid Nahian Chowdhury      | Improvements in the code organization and efficiency, such as reducing redundancy and optimizing payload generation. |
| Preventive Maintenance      | ✓                     | Yew Shu Wen                | Refactor and identify potential system issues to improve long-term reliability.                      |

## Activity-Based Classification Software Maintenance

| Type                   | Implementation Status | Person in Charge      | Justification                                                                                           |
|------------------------|-----------------------|-----------------------|-------------------------------------------------------------------------------------------------------|
| Corrective Maintenance | ✓                     | Abid Nahian Chowdhury | Fixed errors in WebSocket serialization and redundant database queries to ensure proper functionality. |
| Enhancive Maintenance  | ✓                     | Bryan Phang           | Expanded the testing functionality by adding new test functions within the test scripts to improve the system’s testing coverage. |

## Evidence-Based Classification Software Maintenance

| Category         | Type                  | Implementation Status | Person in Charge      | Justification                                                                                           |
|------------------|-----------------------|-----------------------|-----------------------|-------------------------------------------------------------------------------------------------------|
| Business Rules   | Enhancive Maintenance | ✓                     | Yew Shu Wen           | Updated test cases and added new workflows to improve system validation.                              |
|                  | Corrective Maintenance | ✓                     | Yew Shu Wen           | Fix bugs in logic processing.                                                                         |
|                  | Reductive Maintenance  | ✓                     | Yew Shu Wen           | Remove redundant code blocks to reduce complexity.                                                    |
|                  | Preventive Maintenance | ✓                     | Yew Shu Wen           | Refactor workflows to prevent future errors by improving the readability and structure of rules.      |

## Software Properties

| Type                   | Implementation Status | Person in Charge      | Justification                                                                                           |
|------------------------|-----------------------|-----------------------|-------------------------------------------------------------------------------------------------------|
| Adaptive Maintenance   | ✓                     | Koo Song Le           | Migrations have been fixed to ensure consistent deployment between developers.                        |
| Performance Maintenance |                       |                       |                                                                                                       |
| Preventive Maintenance  |                       |                       |                                                                                                       |
| Groomative Maintenance  |                       |                       |                                                                                                       |

## Documentation

| Type                   | Implementation Status | Person in Charge      | Justification                                                                                           |
|------------------------|-----------------------|-----------------------|-------------------------------------------------------------------------------------------------------|
| Reformative Maintenance | ✓                    | Bryan Phang           | Revising existing test scripts and documentation to include new or updated test functions and cases. |

## Support Interface

| Type                   | Implementation Status | Person in Charge      | Justification                                                                                           |
|------------------------|-----------------------|-----------------------|-------------------------------------------------------------------------------------------------------|
| Evaluation Maintenance |                       |                       |                                                                                                       |
| Consultive Maintenance |                       |                       |                                                                                                       |
| Training Maintenance   |                       |                       |                                                                                                       |

---

## Checklist (GitHub Operation)

| Task                         | Implementation Status | Person in Charge           | Justification                                                                                           |
|------------------------------|-----------------------|----------------------------|-------------------------------------------------------------------------------------------------------|
| Create repository            | ✓                     | Koo Song Le                |                                                                                                       |
| Add collaborator (team member) | ✓                   | Koo Song Le                |                                                                                                       |
| Delegate function accordingly | ✓                    | Bryan Phang                | The members are assigned to separate repositories within Deans-Crisis based on proposed maintenance activities. |
| Create branch                | ✓                     | Bryan Phang                | All members have created their own branches on different repositories in Deans-Crisis based on the maintenance activities conducted. |
| Make changes to the code     | ✓                     | Alvin Bradley Nonis        |                                                                                                       |
| Proposed change request      | ✓                     | Phang Hong Boon            | Changes in code should be submitted as pull requests, and receive final review before applying the actual changes. |
| Review change and approve/reject change | ✓          | Phang Hong Boon            | Pull requests are set in place to add one more confirmation step, to ensure quality and accuracy.     |
| Create Workflow (CI file)    | ✓                     | Alvin Bradley Nonis        |                                                                                                       |
| Merge file                   | ✓                     | Phang Hong Boon            |                                                                                                       |
| Baseline (code, branch, etc) | ✓                     | Koo Song Le                |                                                                                                       |
| Update dashboard             | ✓                     | Abid Nahian Chowdhury      |                                                                                                       |

