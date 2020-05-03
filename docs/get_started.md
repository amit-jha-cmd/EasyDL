## Getting Started

__importing the module__
```python
from easedl import Generate
```
The ```Generate``` class is responsible for generating the end to end code. It comes with several methods that can be used to customise and build the pipeline.

__Creating a pipeline__
```python
pipeline = Generate({
    "name": "Model 1",
    "learningRate": 0.01,
    .
    .
    .
})
```
You have to create an object for your pipeline. You can call it whatever you want but I prefer something simple and short.

The ```Generate``` class takes 2 arguments.
1. A ```dictionary```: This contains the configurations regarding the pipeline
2. ```framework```: The framework you want to use to build this pipeline. Currently we only support __PyTorch__.

__What to pass to Generate's ```structure``` argument__
Here is a comprehensive list of currently supported key-value pairs

| Key   |   Type    | Supported valyes  |
|-------|-------|-------------------|
| name  |   String    |  Any string |
| learningRate | float | The learning rate of the model |
| data | dictionary | The dataset configuration, see [this]() |
| test | boolean | Do you want to test after traning |
| layers | dictionary | The configurations for layers, see [this]()|
