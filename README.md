# Sistema de Gestão de Pedidos (Entrega Final)

Projeto console em Java para gerenciar clientes, produtos e pedidos com processamento assíncrono em fila.

## O que foi implementado

- Cadastro de clientes com validação (ID, nome, email).
- Cadastro de produtos com categoria (ENUM Category) e validação de preço.
- Criação de pedidos que contém itens (ProductOrder) e cálculo do total a partir dos itens.
- Processamento assíncrono: pedidos são colocados em uma fila (BlockingQueue) e um OrderProcessor em background retira, muda o status (OrderStatus) para PROCESSANDO, simula tempo de execução e finaliza o pedido.
- Interface: menu de console para gerenciar clientes, produtos, montar carrinho, realizar pedido e listar pedidos (com filtro por status/cliente).

## Arquivos principais

- app/OrderApp.java — interface de console e ponto de entrada.
- model/Customer.java, model/Product.java, model/ProductOrder.java, model/Order.java — modelos de domínio.
- model/Category.java, model/OrderStatus.java — enums.
- service/OrderProcessor.java — fila e thread de processamento (usa LinkedBlockingQueue).
- util/ObjectValidator.java, util/ValidationException.java — validação e exceções customizadas.

## Fundamentos de POO aplicados

- Classes e objetos: cada entidade do domínio é modelada como classe com responsabilidade única.
- Encapsulamento: campos privados e métodos públicos controlando acesso e validação.
- Construtores com validação garantem objetos consistentes desde a criação.
- Uso de enums para representar categorias e estados (melhora legibilidade e segurança).

## SOLID e escolhas de design

- Single Responsibility: OrderProcessor apenas gerencia a fila e processamento; Order, Product e Customer cuidam dos seus dados.
- Open/Closed: novos status/categorias podem ser acrescentados sem mudar lógica do processador.
- Liskov Substitution: não aplicou herança complexa que violaria o princípio.
- Interface Segregation & Dependency Inversion: modules pequenos e coesos; o OrderProcessor é desacoplado da UI.

## Object Calisthenics (pelo menos 3 regras aplicadas)

- Classes pequenas (cada classe tem responsabilidade limitada).
- Métodos curtos: métodos da OrderApp divididos por funcionalidades (CRUD, carrinho, pedidos).
- Evitamos getters/setters triviais quando possível — usamos validação nos setters e construtores para não expor estado inválido.

## Concurrency (como foi tratado)

- A fila de pedidos usa LinkedBlockingQueue (thread-safe), evitando sincronizações manuais.
- OrderProcessor roda em thread daemon separada e processa pedidos usando queue.take() (bloqueante).
- Estados do pedido são representados por OrderStatus (FILA, PROCESSANDO, FINALIZADO) para refletir o fluxo.

## Persistência

Persistência é em memória (listas). Não foi implementado o bônus de salvar/carregar em arquivo — pode ser adicionado como próxima etapa (sugestão: usar JSON com Jackson/Gson).

## Papéis do grupo

- Allan — Implementação da modelagem (classes model/), validações e testes manuais.
- Joao — Interface de console (app/OrderApp.java), integração com OrderProcessor e UX do menu.
- Eduardo — Concorrência e serviço de processamento (service/OrderProcessor.java) e documentação (README).

## Próximos passos sugeridos

- Implementar persistência em arquivo (JSON) com carga/backup ao iniciar/encerrar.
- Adicionar testes automatizados (JUnit) cobrindo validações e processamento.
- Melhorar parsing/validação de e-mail (regex) e mensagens de erro localizadas.

---
Projeto pronto para demonstrar requisitos obrigatórios: OOP, validação, exceções customizadas e processamento assíncrono.
