#include <stdio.h>
#include <math.h>
#include <string.h>

int main()

{
        char seq[100000];
        int length;
        int i;
        float GCcount;

        while( scanf("%s", seq ) == 1)
        {
                length= strlen(seq);
                i=0;
                GCcount=0;
                for(i=0 ; i<length ; i++)
                {

                        if ( seq[i]=='G' || seq[i]=='C' )
                   {
                        GCcount++;
                   }
                }
                printf("GC percentage is %f\n",100*GCcount/length);
        }


}
