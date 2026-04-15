📌 Overview

This project involved building a FastAPI-based Calculation Service using SQLAlchemy, Pydantic, PostgreSQL, Docker, and GitHub Actions CI/CD. The goal was to implement clean backend architecture with proper testing and deployment practices.

🧠 Key Learning Points

I learned how to design and connect SQLAlchemy models with a PostgreSQL database, and how Pydantic schemas help enforce strict input validation. Implementing the factory pattern helped improve code structure by separating arithmetic operations into modular components.

⚠️ Challenges Faced

One major challenge was handling database-related issues during testing, such as connection errors and session rollback problems. I also faced IntegrityError issues due to duplicate test data, which I resolved by using unique values for each test.

Another challenge was managing pytest fixtures correctly to ensure proper database isolation between tests. Initially, test data was not visible or was causing session conflicts, which required fixing transaction handling.

🧪 Testing & CI/CD

I implemented both unit and integration tests. Unit tests validated schema rules and factory logic, while integration tests confirmed database operations. Setting up GitHub Actions with PostgreSQL helped automate testing and ensure code reliability before deployment.

🚀 Conclusion

This project improved my understanding of backend development, especially in database integration, testing strategies, and CI/CD pipelines. Debugging real-world issues helped strengthen my problem-solving skills and understanding of production-ready backend systems.