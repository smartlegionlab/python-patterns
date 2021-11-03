# Python Patterns

***

![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/python-patterns)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/python-patterns)](https://github.com/smartlegionlab/python-patterns/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/python-patterns)](https://github.com/smartlegionlab/python-patterns/blob/master/LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/python-patterns?style=social)](https://github.com/smartlegionlab/python-patterns/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/python-patterns?style=social)](https://github.com/smartlegionlab/python-patterns/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/python-patterns?style=social)](https://github.com/smartlegionlab/python-patterns/)


***

## Help the project financially:

- PayPal: [https://paypal.me/smartlegionlab](https://paypal.me/smartlegionlab)
- Yandex Money: [https://yoomoney.ru/to/4100115206129186](https://yoomoney.ru/to/4100115206129186)
- LiberaPay: [https://liberapay.com/smartlegion/donate](https://liberapay.com/smartlegion/donate)
- Visa: 4048 0250 0089 5923

***

## Short description:

___python-patterns___ - A collection of design patterns and idioms in Python (With tests!).

****

## Current Patterns

__Creational Patterns__:

| Pattern | Description | Tests |
|:-------:| ----------- |------|
| [Abstract Factory](patterns/creational/abstract_factory.py) | use a generic function with specific factories | [test](tests/test_creational/test_abstract_factory.py) |
| [Builder](patterns/creational/builder.py) | instead of using multiple constructors, builder  receives parameters and returns constructed objects | [test](tests/test_creational/test_builder.py) |
| [Factory Method](patterns/creational/factory.py) | delegate a specialized function/method to create instances|  [test](tests/test_creational/test_factory.py) |
| [Prototype](patterns/creational/prototype.py) | use a factory and clones of a prototype for new instances (if instantiation is expensive) | [test](tests/test_creational/test_prototype.py) |
| [Singleton](patterns/creational/singleton.py) | Ensures that the class has only one instance, and provides a global access point to it. | [test](tests/test_creational/test_singleton.py) |

__Structural Patterns__:

| Pattern | Description | Tests |
|:-------:| ----------- |------|
| [Adapter](patterns/structural/adapter.py) | converts the interface of one class to the interface of another that clients expect. | [test](tests/test_structural/test_adapter.py) |
| [Bridge](patterns/structural/bridge.py) | a client-provider middleman to soften interface changes | [test](tests/test_structural/test_bridge.py) |
| [Composite](patterns/structural/composite.py) | lets clients treat individual objects and compositions uniformly | [test](tests/test_structural/test_composite.py) |
| [Decorator](patterns/structural/decorator.py) | wrap functionality with other functionality in order to affect outputs | [test](tests/test_structural/test_decorator.py) |
| [Facade](patterns/structural/facade.py) | use one class as an API to a number of others | [test](tests/test_structural/test_facade.py) |
| [Flyweight](patterns/structural/flyweight.py) | transparently reuse existing instances of objects with similar/identical state | [test](tests/test_structural/test_flyweight.py) |
| [Proxy](patterns/structural/proxy.py) | an object funnels operations to something else | [test](tests/test_structural/test_proxy.py) |

__Behavior Patterns__:

| Pattern | Description | Tests |
|:-------:| ----------- |------|
| [Blackboard](patterns/behavioral/blackboard.py) | architectural model, assemble different sub-system knowledge to build a solution, AI approach - non gang of four pattern. | [test](tests/test_behovioral/test_blackboard.py) |
| [chain_of_responsibility](patterns/behavioral/chain_of_responsibility.py) | apply a chain of successive handlers to try and process the data. | [test](tests/test_behovioral/test_chain_of_responsibility.py) |
| [command](patterns/behavioral/command.py) | bundle a command and arguments to call later. | [test](tests/test_behovioral/test_command.py) |
| [interpreter](patterns/behavioral/interpreter.py) | a behavioral design pattern that solves a frequently encountered but subject to change problem. | [test](tests/test_behovioral/test_interpreter.py) |
| [iterator](patterns/behavioral/iterator.py) | traverse a container and access the container's elements. | [test](tests/test_behovioral/test_iterator.py) |
| [mediator](patterns/behavioral/mediator.py) | an object that knows how to connect other objects and act as a proxy. | [test](tests/test_behovioral/test_mediator.py) |
| [memento](patterns/behavioral/memento.py) | generate an opaque token that can be used to go back to a previous state. | [test](tests/test_behovioral/test_memento.py) |
| [observer](patterns/behavioral/observer.py) | provide a callback for notification of events/changes to data. | [test](tests/test_behovioral/test_observer.py) |
| [state](patterns/behavioral/state.py) | logic is organized into a discrete number of potential states and the next state that can be transitioned to. | [test](tests/test_behovioral/test_state.py) |
| [strategy](patterns/behavioral/strategy.py) | selectable operations over the same data. | [test](tests/test_behovioral/test_strategy.py) |
| [template_method](patterns/behavioral/template_method.py) |defines the basis of the algorithm and allows subclasses to override some of the steps in the algorithm, without changing its structure as a whole. | [test](tests/test_behovioral/test_template_method.py) |
| [visitor](patterns/behavioral/visitor.py) | invoke a callback for all items of a collection. | [test](tests/test_behovioral/test_template_visitor.py) |

***

# Help:

### Requirements:

- [python](https://python.org) 3.6+

For run tests:

- pytest
    - `pip3 install pytest`
    - `pytest -v`
    
- pytest-cov
    - `pip3 install pytest-cov`
    - `pytest --cov`

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
