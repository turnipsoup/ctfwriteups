# Whale Watching

### Challenge Text

>Where is the flag? It is not down on any map; true places never are.
>Hunt down:
>`johnhammond/whale_watching`

### Challenge Work

Whale watching....that format also looks familiar....

```
~ % docker pull johnhammond/whale_watching
```

```
~ % docker inspect johnhammond/whale_watching
[
    {
        "Id": "sha256:caf5b6f9a508753559f460cca815ba154560dca5db712da0a31fcf5bf61928e1",
        "RepoTags": [
            "johnhammond/whale_watching:latest"
        ],
        "RepoDigests": [
            "johnhammond/whale_watching@sha256:2b7db5e2796fbbd0616d5279b81f0ae151f4a52ad3e0325de7f583ce94848ddd"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2020-07-21T18:46:55.1580955Z",
        "Container": "4d887a53ffaf63aaeb6de6ab789cb63903de6394076eda1caa0a72cef4f1eec2",
        "ContainerConfig": {
            "Hostname": "9ec8c01a6a48",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "echo \"flag{call_me_ishmael}\" > /dev/null"
            ],
            "Image": "sha256:6b362a9f73eb8c33b48c95f4fcce1b6637fc25646728cf7fb0679b2da273c3f4",
            "Volumes": null,
            "WorkingDir": "/cowsay",
            "Entrypoint": null,
            "OnBuild": [],
            "Labels": {}
        },
        "DockerVersion": "19.03.8",
        "Author": "",
        "Config": {
            "Hostname": "9ec8c01a6a48",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/bash"
            ],
            "Image": "sha256:6b362a9f73eb8c33b48c95f4fcce1b6637fc25646728cf7fb0679b2da273c3f4",
            "Volumes": null,
            "WorkingDir": "/cowsay",
            "Entrypoint": null,
            "OnBuild": [],
            "Labels": {}
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 247049019,
        "VirtualSize": 247049019,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/7f795f9d08b0ac44261c2b56f4a30ae29bddb89c69a1d75590defa88c5aaec33/diff:/var/lib/docker/overlay2/fffd497d82b48d90bc45454469b774e0f6e831c7ebbe3e1cd3b8caa2db9f46b1/diff:/var/lib/docker/overlay2/957cfcf3a6d43624eff4fa61db51aab7843adc5473925b80c0f23694e5ba5802/diff:/var/lib/docker/overlay2/f16797ae8423237ff60468b88c86fdf1708e96a16ea073877e32f86ee796422c/diff:/var/lib/docker/overlay2/6f3ebe3833fafd3d9a5ed11ef8324e3e7d6da2ded7d523f68d224130939ceb6d/diff:/var/lib/docker/overlay2/b999c127f3485e563017bb889b7eb53b70053be97788644816afa7999216b02d/diff:/var/lib/docker/overlay2/e50edf4a31c43270f63116258015960e94cd66776c60e7b047009bdff2e32f84/diff:/var/lib/docker/overlay2/4dc9051483fccc9fc3880a2a024700382b224d416f6993ed85291e1f6cbebd61/diff:/var/lib/docker/overlay2/948524549a6d891d2778d1eaf8910254fd0d7d0f78e7249e8f33be364672c87b/diff",
                "MergedDir": "/var/lib/docker/overlay2/cdc27c8504bfd4e461db383cc7656babff10b3b272c7d9c280f1c878f14cce0b/merged",
                "UpperDir": "/var/lib/docker/overlay2/cdc27c8504bfd4e461db383cc7656babff10b3b272c7d9c280f1c878f14cce0b/diff",
                "WorkDir": "/var/lib/docker/overlay2/cdc27c8504bfd4e461db383cc7656babff10b3b272c7d9c280f1c878f14cce0b/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:1154ba695078d29ea6c4e1adb55c463959cd77509adf09710e2315827d66271a",
                "sha256:528c8710fd95f61d40b8bb8a549fa8dfa737d9b9c7c7b2ae55f745c972dddacd",
                "sha256:37ee47034d9b78f10f0c5ce3a25e6b6e58997fcadaf5f896c603a10c5f35fb31",
                "sha256:5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef",
                "sha256:b26122d57afa5c4a2dc8db3f986410805bc8792af3a4fa73cfde5eed0a8e5b6d",
                "sha256:091abc5148e4d32cecb5522067509d7ffc1e8ac272ff75d2775138639a6c50ca",
                "sha256:5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef",
                "sha256:d511ed9e12e17ab4bfc3e80ed7ce86d4aac82769b42f42b753a338ed9b8a566d",
                "sha256:d061ee1340ecc8d03ca25e6ca7f7502275f558764c1ab46bd1f37854c74c5b3f",
                "sha256:5f70bf18a086007016e948b04aed3b82103a36bea41755b6cddfaf10ace3c6ef"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]
```

You can see our flag is in the CMD variable of one of the layers:

>flag{call_me_ishmael}