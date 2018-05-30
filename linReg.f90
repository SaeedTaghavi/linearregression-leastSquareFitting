program linearRegresion
        implicit none
        integer:: N, i !N is number of data points, read it at the first line of data file
        real , dimension(:), allocatable::x,y
        real::b,m,x_mean,y_mean


!        print *,"sum", sum(x*y)
        !the * for to vectors will apply like the following argument
!        s=0.
!        do i=1,7
!            s=s+x(i)*y(i)
!        end do
!        print*,"s",s


!       Reading data from file
        open(unit=77,file='data')
        read(77,*)N
        allocate(x(N),y(N))

        do i=1,N
           read(77,*)x(i),y(i)
        end do
        close(77)

!       LinearRegression
        y_mean = sum(y)/real(size(y))
        x_mean = sum(x)/real(size(x))
        m=(sum(x*y)-(y_mean*sum(x)))/(sum(x**2.0)-(x_mean*sum(x)))
        b=y_mean-m*x_mean 
        
        print*,"number of data points: ",n
        print*,"slope: m=",m
        print*,"b=",b
        
        open (55,file='result')
        write(55,*) n , "number of data points"
        write(55,*) m, "slope of the line"
        write(55,*) b, "b "

end
