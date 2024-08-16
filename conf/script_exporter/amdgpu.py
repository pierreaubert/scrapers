#!/usr/bin/python3

import subprocess
import pprint

def cleanup_value(value: str) -> str:
    split = value.split(' ')
    return split[0]

def parse_gpu(lines: list[str]) -> tuple[int, dict]:
    gpu = {}
    section = ''
    for i, line in enumerate(lines):
        if line[0:3] == "GPU":
            return i, gpu
        sline = line.split(':')
        ln = len(sline)
        if ln == 1 or (ln == 2 and len(sline[1])==0):
            section = sline[0].strip().lower()
        elif len(sline) == 2:
            value = sline[1].strip().lower()
            if 'n/a' in value:
                continue
            key = '{}_{}'.format(section, sline[0].strip().lower())
            gpu[key] = cleanup_value(value)
    return -1, gpu

def parse(lines : list[str])->list[dict]:

    gpus = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if line[0:3] == 'GPU':
            ilast, gpu = parse_gpu(lines[i+1:])
            gpus.append(gpu)
            if ilast == -1:
                break
            i += ilast
        i += 1

    return gpus

def print_metric(name, doc, kind, value):
    print('# HELP {} "{}"'.format(name, doc.replace('_', ' ')))
    print('# TYPE {} {}'.format(name, kind))
    print('{} {}'.format(name, value))

def prometheus(gpus):
    for i, gpu in enumerate(gpus):
        for key in (
                'power_socket_power',
                'temperature_edge',
                'temperature_hotspot',
                'temperature_mem',
                'fan_speed',
                'fan_rpm',
                'mem_usage_vram',
                'mem_usage_free',
                'usage_gfx_activity',
                'usage_umc_activity',
                'usage_mm_activity',
        ):
            if not key in gpu:
                continue
            print_metric('amd_gpu_{}'.format(key),
                         key,
                         "gauge",
                         gpu[key])

output = subprocess.run(["/usr/bin/amd-smi", "metric"], shell=False, capture_output=True, check=True, text=True)
gpus = parse(output.stdout.split('\n'))
# pprint.pp(gpus)
prometheus(gpus)

