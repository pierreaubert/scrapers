# Prometheus scrapers

Various prometheus scrapers for my homelab (nvidia, amd gpu, etc)
This is more for me than usable by others but it can serve as example.
The CLI parsers are generic and call easily be reused.

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

## Script Exporter

via https://github.com/ricoberger/script_exporter

## HP SSA Cli

`hpssacli` is still available from HP.
I parsed the output via `script_exporter`.

# Prometheus and Victoria configuration

to be added


