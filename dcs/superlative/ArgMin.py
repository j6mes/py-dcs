class ArgMin():
    def __init__(self, u, b):
        self.u = u
        self.b = b

    def __str__(self):
        return "[ARGMIN: " + str(self.u) + " " + str(self.b) + "]"

    def compile(self):
        return lambda x: x in self.vals()

    def vals(self):
        bc = self.b.compile()
        current_min = float("inf")

        best_v = set()
        for uv in self.u.vals():
            for bv in self.b.vals():
                m = bc(uv, bv.v)

                if isinstance(bv.v.value, str):
                    return None

                if m and bv.v.value < current_min:
                    current_min = bv.v.value
                    best_v = {uv}
                elif m and bv.v.value == current_min:
                    best_v.add(uv)

        if best_v is not None:
            return best_v

        return None
