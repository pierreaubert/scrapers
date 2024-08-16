# scrapers

various prometheus scrapers for my homelab (nvidia, amd gpu, etc)

## GPUs

### Nvidia

via https://github.com/utkuozdemir/nvidia_gpu_exporter

### AMD

`amdgpu-cli` is provided by your distro.
I parsed the output and use `script_exporter`

## Speedtest

`speedtest` from ookla.
I parsed the output and use  `script_exporter`

## Mikrotik

via https://github.com/akpw/mktxp

## Coinmarketcap

via https://github.com/bonovoxly/coinmarketcap-exporter

## FoundationDB

via https://hub.docker.com/r/aikoven/foundationdb-exporter
