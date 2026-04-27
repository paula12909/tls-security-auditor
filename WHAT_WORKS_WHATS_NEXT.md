# What Works / What’s Next

## What Works

The TLS Security Auditor is fully operational as an end-to-end system running inside a Docker environment. The project successfully demonstrates a complete vertical slice from service deployment to analysis and artifact generation.

The system is able to:
- Launch secure and insecure TLS services using Docker containers
- Scan each service and extract TLS configuration data, including protocol version, cipher suite, and certificate presence
- Detect insecure configurations such as missing certificates or failed TLS handshakes
- Assign risk scores and classify results as LOW or HIGH risk
- Compare multiple targets and determine which configuration is more secure
- Generate output artifacts including logs, JSON summaries, CSV metrics, and comparison results
- Execute reliably using a single command: `make up && make demo`

In addition, the project includes automated testing with multiple unit and integration tests, as well as a CI pipeline that builds the project and runs tests with coverage reporting.

All outputs are reproducible and stored in the `artifacts/release/` directory, ensuring that results can be reviewed and validated.

---

## What’s Next

The next phase of the project will focus on expanding evaluation and improving analysis depth.

Planned improvements include:
- Expanding the dataset of TLS scan results to include additional configurations
- Adding more edge-case and negative test scenarios to improve coverage
- Creating visual charts or tables to better present evaluation results
- Enhancing TLS validation logic, including deeper certificate analysis and protocol enforcement
- Improving reporting and formatting of output artifacts for clarity and usability

Future work will also include refining the evaluation results and documenting findings in more detail for the final submission.

Overall, the system is stable and functional, and future work will focus on improving accuracy, coverage, and presentation of results.
