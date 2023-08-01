code_summary_description = {
    "name": "code_summary",
    "description": "Get a files functions and it's external dependencies.",
    "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "The path to the file. The path should not start with . or .. or / or ~. The project root is added to the path automatically."
                }
            }
    }
}
