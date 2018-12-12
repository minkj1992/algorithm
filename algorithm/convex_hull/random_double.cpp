// rand - disk - points . cpp
// MCS 481 project 1 description version 1.0
# include < cstdlib >
# include < ctime >
# include < cmath >
# include < iostream >
using namespace std ;
double dblrand () // return pseudorandom double in [0.0 ,1.0).
{
return rand ()/( double ( RAND_MAX ) + 1);
}
int main (){
    srand (( unsigned ) time (0)); // Seed the random generator with current time
    const int numpoints = 50;
    for ( int i =0; i < numpoints ; i ++) {
        // Generate points in the square [ -1 ,1) x [ -1 ,1) until we find one
        // that lies in the unit disk .
        // This is not an efficient algorithm ( it has infinite worst - case
        // running time !) but we use it because the code is particularly
        // simple and efficiency of this component is not a focus of the
        // project .
        double x , y ;
        do {
            x = 2.0* dblrand () - 1.0; // rescale to get random number in [ -1 ,1)
            y = 2.0* dblrand () - 1.0;
        } while ( fabs ( x * x + y * y ) > 1.0);
        cout << x << " " << y << endl ;
    }
}