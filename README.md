IS218 Final Project Reflection Document
This project gave me hands-on experience developing and managing a user management system using Python and FastAPI. This project deepened my understanding of REST API design, including adding filtering and search capabilities to improve usability. Furthermore, using Git and GitHub for version control and collaborating through issues and pull requests helped me practice professional software development workflows. I also learned how to address challenges associated with embedded Git repositories and Docker configuration for continuous integration.
I implemented user search and filtering functionality (branch: feature/user-search). This feature allows users to search and filter the user list based on parameters such as registration date. Adding this functionality improves system usability by making data retrieval and management more efficient. It addresses a key missing feature in the original system, so I improved it and laid the foundation for future user management improvements.
Links to 5 QA Issue Fixes
1.	Allows self-deletion (#10)
2.	Allows arbitrarily large limit value (#9)
3.	Allows empty or weak password (#8)
4.	Can’t register second user — "connection_unexpectedly_closed" (#7)
5.	Nickname in register request is not respected (#6)
Links to 10 New Tests (Issues / Commits)
•	Fix Docker file due to installation failure — commit fdacbae
•	Add test cases to test_user_schemas.py — commit b56d32b
•	Enhance user_service.py to support search and filtering — commit 4d6e7dd
•	Add search and filtering features — commit ad4d4d1
•	Add three more test cases to test_user_model.py — commit ec81543
•	Add API test cases for search feature and fix bugs — commit 013b5b4
•	Avoid sending email verification for now — commit fc04e6d
•	Refactor search API — commit 286cb39
•	Add registration date range filtering to list users API — commit b570967
•	Add service test cases for filtering and search features — commit ffe2042
New Feature
Add Feature #3 User Search and Filtering #11
https://github.com/cycy3114/user_management/pull/11
DockerHub Image
https://hub.docker.com/r/yc228/user_management/tags
This was a challenging yet exciting exercise. It was incredibly rewarding. Not only did the exercise allow me to review all the knowledge I'd gained throughout the course, but it also kept me thinking about and solving problems. A major challenge I encountered was dealing with the embedded Git repository in the .github/workflows/user_management directory, which caused issues when staging files and pushing commits. After thinking about how to address this, I solved the problem by removing the nested .git folder from the directory and re-adding the files as regular project files. This ensured smooth version control and avoided submodule conflicts. Another challenge was writing comprehensive tests to cover the new search and filtering functionality. By designing API and service layer tests and using the pytest testing tool, I achieved strong test coverage, which helped me detect errors early and ensured system reliability. Furthermore, I resolved a Docker image build failure by updating the Dockerfile and dependencies, successfully running the CI/CD pipeline and deploying the container.

