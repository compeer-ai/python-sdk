# Alive

Types:

```python
from compeer.types import AliveCheckResponse
```

Methods:

- <code title="get /alive">client.alive.<a href="./src/compeer/resources/alive.py">check</a>() -> <a href="./src/compeer/types/alive_check_response.py">AliveCheckResponse</a></code>

# Oidc

Types:

```python
from compeer.types import OidcRetrieveResponse
```

Methods:

- <code title="get /oidc">client.oidc.<a href="./src/compeer/resources/oidc.py">retrieve</a>() -> <a href="./src/compeer/types/oidc_retrieve_response.py">OidcRetrieveResponse</a></code>

# Backup

Types:

```python
from compeer.types import BackupRetrieveResponse
```

Methods:

- <code title="get /backup">client.backup.<a href="./src/compeer/resources/backup.py">retrieve</a>() -> <a href="./src/compeer/types/backup_retrieve_response.py">BackupRetrieveResponse</a></code>

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
from compeer.types import SearchGetStoresResponse
```

Methods:

- <code title="get /{workspace}/search">client.search.<a href="./src/compeer/resources/search.py">get_stores</a>(workspace, \*\*<a href="src/compeer/types/search_get_stores_params.py">params</a>) -> <a href="./src/compeer/types/search_get_stores_response.py">SearchGetStoresResponse</a></code>

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
