
def add_external_factors(X, *features):
   for f in features:
      X = X.join(f)


