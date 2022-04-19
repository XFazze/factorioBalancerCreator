# TODO create system
# TODO crate example
# TODO test example
# TODO prettyprint

from create.createBalancerMain import createBalancer


def main():
    size = {
        'height': 4,
        'width': 4
    }
    belts = {
        'in': 2,
        'out': 2
    }
    balancer = createBalancer(size, belts)

    print(balancer)


if __name__ == "__main__":
    main()
