test:
	# Run tests for each rule file
	semgrep --test
	# Lint the test files themselves
	semgrep --validate --config .

