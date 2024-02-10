import kopf
import asyncio
import datetime
from kasa import SmartPlug, SmartBulb

@kopf.on.create('kvecchione.dev', 'v1','kasalights')
@kopf.on.update('kvecchione.dev', 'v1','kasalights')
def handle(meta, spec, namespace, logger, body, **kwargs):
    ip = spec.get('ip')
    type = spec.get('type')
    state = spec.get('state')
    name = meta.get('name')

    if type == 'plug':
        dev = SmartPlug(ip)
    elif type == 'bulb':
        dev = SmartBulb(ip)
    else:
        logger.info(f"Type not supported: %s", type)
        return {'result': f'error, invalid type specified {type}'}

    if state == 'on':
        asyncio.run(dev.turn_on())
    elif state == 'off':
        asyncio.run(dev.turn_off())
    else:
        logger.info(f"Invalid state: %s", state)
        return {'result': f'error, invalid state specified {state}'}

    current_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    kopf.event(
        body, 
        type='Update',
        reason="state changed", 
        message=f'{name} turned {state} at {current_time}'
    )
    
    return {'result': f'{name} turned {state} at {current_time}'}
    
