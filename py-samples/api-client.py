from dataclasses import dataclass


@dataclass
class ApiResponse:
    status_code: int
    payload: dict


class ApiClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")

    def get_status(self) -> ApiResponse:
        return ApiResponse(
            status_code=200,
            payload={
                "service": "copilot-cli-playground",
                "status": "ok",
                "base_url": self.base_url,
            },
        )


if __name__ == "__main__":
    client = ApiClient("https://api.example.com")
    response = client.get_status()
    print(response)
