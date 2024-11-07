from fastapi.responses import JSONResponse
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from uuid import  UUID

def success_response(message: str, data=None, code="operation_successful", status_code=HTTP_200_OK):
    try:
        if hasattr(data, "model_dump"):  # Pydantic v2
            data = data.model_dump()
        elif hasattr(data, "dict"):  # Pydantic v1
            data = data.dict()

        response_content = {
            "status": "success",
            "code": code,
            "message": message,
            "data": data
        }
        return JSONResponse(
            status_code=status_code,
            content=response_content,
        )
    except Exception as e:
        print("Serialization Error:", e)
        return JSONResponse(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status": "error",
                "code": "serialization_error",
                "message": str(e),
                "data": None
            },
        )


def success_get(data, message="Data retrieved successfully"):
    if hasattr(data, "model_dump"):
        data = data.model_dump()

    # Convert UUIDs to strings in the response data
    def convert_uuid(obj):
        if isinstance(obj, UUID):
            return str(obj)
        elif isinstance(obj, dict):
            return {k: convert_uuid(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_uuid(i) for i in obj]
        return obj

    data = convert_uuid(data)
    return success_response(
        message=message,
        data=data,
        code=HTTP_200_OK,
        status_code=HTTP_200_OK
    )

def success_post(data, message="Data created successfully"):
    if hasattr(data, "model_dump"):
        data = data.model_dump()

    # Convert UUIDs to strings in the response data
    def convert_uuid(obj):
        if isinstance(obj, UUID):
            return str(obj)
        elif isinstance(obj, dict):
            return {k: convert_uuid(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_uuid(i) for i in obj]
        return obj

    data = convert_uuid(data)

    return success_response(
        message=message,
        data=data,
        code=HTTP_201_CREATED,
        status_code=HTTP_201_CREATED
    )

def success_put(data, message="Data updated successfully"):
    if hasattr(data, "model_dump"):
        data = data.model_dump()

    # Convert UUIDs to strings in the response data
    def convert_uuid(obj):
        if isinstance(obj, UUID):
            return str(obj)
        elif isinstance(obj, dict):
            return {k: convert_uuid(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_uuid(i) for i in obj]
        return obj

    data = convert_uuid(data)
    return success_response(
        message=message,
        data=data,
        code=HTTP_200_OK,
        status_code=HTTP_200_OK
    )

def success_delete(message="Data deleted successfully"):
    return success_response(
        message=message,
        data=None,
        code=HTTP_204_NO_CONTENT,
        status_code=HTTP_204_NO_CONTENT
    )