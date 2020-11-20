
class WeightBasedSorter( object ):

    def sort( self, viewlets ):
        return sorted( viewlets,
                       lambda x, y: cmp(x[1].weight, y[1].weight ) )
