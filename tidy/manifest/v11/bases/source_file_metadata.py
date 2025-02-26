from pydantic import BaseModel, ConfigDict, Field


class FileSlice(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    filename: str
    content: str
    start_line_number: int
    end_line_number: int


class SourceFileMetadata(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    repo_file_path: str
    file_slice: FileSlice = Field(..., title="FileSlice")
