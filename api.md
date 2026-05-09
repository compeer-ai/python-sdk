# Projects

Types:

```python
from barque.types import ProjectReadAllResponse
```

Methods:

- <code title="get /api/v1/projects">client.projects.<a href="./src/barque/resources/projects.py">read_all</a>() -> <a href="./src/barque/types/project_read_all_response.py">ProjectReadAllResponse</a></code>

# Captures

Types:

```python
from barque.types import CaptureCreateResponse, CaptureSearchResponse
```

Methods:

- <code title="post /api/v1/capture">client.captures.<a href="./src/barque/resources/captures.py">create</a>(\*\*<a href="src/barque/types/capture_create_params.py">params</a>) -> <a href="./src/barque/types/capture_create_response.py">CaptureCreateResponse</a></code>
- <code title="get /api/v1/search">client.captures.<a href="./src/barque/resources/captures.py">search</a>(\*\*<a href="src/barque/types/capture_search_params.py">params</a>) -> <a href="./src/barque/types/capture_search_response.py">CaptureSearchResponse</a></code>
