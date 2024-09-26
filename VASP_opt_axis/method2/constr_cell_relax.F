      SUBROUTINE CONSTR_CELL_RELAX(FCELL)
      USE PREC
      REAL(Q) FCELL(3,3), SAVE(3)
      LOGICAL FILFLG
      INTEGER ICELL(3)

      INQUIRE(FILE='OPTCELL',EXIST=FILFLG)
      IF (FILFLG) THEN
        OPEN(67,FILE='OPTCELL',FORM='FORMATTED',STATUS='OLD')
          READ(67,"(3I1)") (ICELL(I),I=1,3)
        CLOSE(67)
        DO I=1,3
          SAVE(I)=FCELL(I,I)
        ENDDO
        FCELL=0.0d0
        DO I=1,3
          IF (ICELL(I)==1) FCELL(I,I)=SAVE(I)
        ENDDO
      ENDIF

!     just one simple example
!     relaxation in x directions only
!      SAVE=FCELL(1,1)
!      FCELL=0   ! F90 style: set the whole array to zero
!      FCELL(1,1)=SAVE

      RETURN
      END SUBROUTINE