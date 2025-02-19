from pydantic import BaseModel


class FileSlice(BaseModel):
    filename: str
    content: str
    start_line_number: int
    end_line_number: int


class SourceFileMetadata(BaseModel):
    repo_file_path: str
    file_slice: FileSlice