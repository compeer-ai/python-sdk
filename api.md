# Alive

Types:

```python
from compeer.types import AliveCheckResponse
```

Methods:

- <code title="get /alive">client.alive.<a href="./src/compeer/resources/alive.py">check</a>() -> <a href="./src/compeer/types/alive_check_response.py">AliveCheckResponse</a></code>

# Stores

Types:

```python
from compeer.types import StoreListResponse
```

Methods:

- <code title="get /{workspace}/stores">client.stores.<a href="./src/compeer/resources/stores.py">list</a>(workspace) -> <a href="./src/compeer/types/store_list_response.py">StoreListResponse</a></code>

# Search

Types:

```python
from compeer.types import SearchQueryResponse
```

Methods:

- <code title="get /{workspace}/search">client.search.<a href="./src/compeer/resources/search.py">query</a>(workspace, \*\*<a href="src/compeer/types/search_query_params.py">params</a>) -> <a href="./src/compeer/types/search_query_response.py">SearchQueryResponse</a></code>

# Workspaces

Types:

```python
from compeer.types import WorkspaceListResponse
```

Methods:

- <code title="get /workspaces">client.workspaces.<a href="./src/compeer/resources/workspaces.py">list</a>() -> <a href="./src/compeer/types/workspace_list_response.py">WorkspaceListResponse</a></code>

# Capture

Types:

```python
from compeer.types import CaptureCreateResponse
```

Methods:

- <code title="post /{workspace}/capture">client.capture.<a href="./src/compeer/resources/capture.py">create</a>(workspace, \*\*<a href="src/compeer/types/capture_create_params.py">params</a>) -> <a href="./src/compeer/types/capture_create_response.py">CaptureCreateResponse</a></code>
