write_to_file_description = {
    "name": "write_to_file",
    "description": "Write to a specified file.",
    "parameters": {
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "The path to the file. Cannot start with . or .. or / or ~. Project root is added to the path automatically."
            },
            "content": {
                "type": "string",
                "description": "The content to write into the file."
            }
        }
    }
}