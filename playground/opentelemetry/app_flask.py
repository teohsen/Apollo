import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    BatchSpanProcessor,
)

from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

load_dotenv('playground/opentelemetry')


# Get settings from .env file
service_name = os.getenv("OTEL_SERVICE_NAME")
tracer_exporter = os.getenv("OTEL_TRACES_EXPORTER")
metrics_exporter = os.getenv("OTEL_METRICS_EXPORTER")
logs_exporter = os.getenv("OTEL_LOGS_EXPORTER")
tracer_sampler = os.getenv("OTEL_TRACES_SAMPLER")
excluded_urls = os.getenv("OTEL_PYTHON_REQUESTS_EXCLUDED_URL")


resource = Resource(attributes={"service.name": "playgroundopentelemetryflask"})
tprovider = TracerProvider(resource=resource)
tprovider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

trace.set_tracer_provider(tprovider)
tracer = trace.get_tracer(__name__)


app = Flask(__name__)

FlaskInstrumentor().instrument_app(app, excluded_urls=excluded_urls)
RequestsInstrumentor().instrument()
#RequestsInstrumentor().instrument(excluded_urls=excluded_urls)


@app.route("/")
def hello():
    import requests
    response = requests.get("https://api.nusmods.com/v2/2023-2024")

    return f"opentelemetry: get request to: {response.status_code = }"


if __name__ == "__main__":
    app.run(debug=True)


"""
127.0.0.1 - - [19/Apr/2024 15:34:59] "GET / HTTP/1.1" 200 -
{
    "name": "GET",
    "context": {
        "trace_id": "0x6070d1f9079c3f17368b9b6d283ddec2",
        "span_id": "0xc7e0b27e8bba1dc9",
        "trace_state": "[]"
    },
    "kind": "SpanKind.CLIENT",
    "parent_id": "0x8ce35e6f57ea815d",
    "start_time": "2024-04-19T07:34:58.766298Z",
    "end_time": "2024-04-19T07:34:59.468288Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
        "http.method": "GET",
        "http.url": "https://api.nusmods.com/v2/2023-2024",
        "http.status_code": 200
    },
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "service.name": "playgroundopentelemetryflask"
        },
        "schema_url": ""
    }
}
{
    "name": "/",
    "context": {
        "trace_id": "0x6070d1f9079c3f17368b9b6d283ddec2",
        "span_id": "0x8ce35e6f57ea815d",
        "trace_state": "[]"
    },
    "kind": "SpanKind.SERVER",
    "parent_id": null,
    "start_time": "2024-04-19T07:34:58.758297Z",
    "end_time": "2024-04-19T07:34:59.469289Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "service.name": "playgroundopentelemetryflask"
        },
        "schema_url": ""
    }
}


"""