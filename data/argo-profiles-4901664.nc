CDF      
      	DATE_TIME         	STRING256         STRING64   @   STRING32       STRING16      STRING8       STRING4       STRING2       N_PROF        N_PARAM       N_LEVELS  �   N_CALIB       	N_HISTORY             	   title         Argo float vertical profile    institution       AOML   source        
Argo float     history       2015-07-06T19:20:57Z creation      
references        (http://www.argodatamgt.org/Documentation   comment           user_manual_version       3.03   Conventions       Argo-3.0 CF-1.6    featureType       trajectoryProfile         @   	DATA_TYPE                  	long_name         	Data type      
_FillValue                    5�   FORMAT_VERSION                 	long_name         File format version    
_FillValue                    5�   HANDBOOK_VERSION               	long_name         Data handbook version      
_FillValue                    5�   REFERENCE_DATE_TIME                 	long_name         !Date of reference for Julian days      conventions       YYYYMMDDHHMISS     
_FillValue                    5�   DATE_CREATION                   	long_name         Date of file creation      conventions       YYYYMMDDHHMISS     
_FillValue                    5�   DATE_UPDATE                 	long_name         Date of update of this file    conventions       YYYYMMDDHHMISS     
_FillValue                    5�   PLATFORM_NUMBER                   	long_name         Float unique identifier    conventions       WMO float identifier : A9IIIII     
_FillValue                    5�   PROJECT_NAME                  	long_name         Name of the project    
_FillValue                  �  5�   PI_NAME                   	long_name         "Name of the principal investigator     
_FillValue                  �  6|   STATION_PARAMETERS           	            	long_name         ,List of available parameters for the station   conventions       Argo reference table 3     
_FillValue                  `  6�   CYCLE_NUMBER               	long_name         Float cycle number     conventions       <0..N, 0 : launch cycle (if exists), 1 : first complete cycle   
_FillValue         ��        7\   	DIRECTION                  	long_name         !Direction of the station profiles      conventions       -A: ascending profiles, D: descending profiles      
_FillValue                    7d   DATA_CENTRE                   	long_name         .Data centre in charge of float data processing     conventions       Argo reference table 4     
_FillValue                    7h   DC_REFERENCE                  	long_name         (Station unique identifier in data centre   conventions       Data centre convention     
_FillValue                  @  7l   DATA_STATE_INDICATOR                  	long_name         1Degree of processing the data have passed through      conventions       Argo reference table 6     
_FillValue                    7�   	DATA_MODE                  	long_name         Delayed mode or real time data     conventions       >R : real time; D : delayed mode; A : real time with adjustment     
_FillValue                    7�   PLATFORM_TYPE                     	long_name         Type of float      
_FillValue                  @  7�   FLOAT_SERIAL_NO                   	long_name         Serial number of the float     
_FillValue                     7�   FIRMWARE_VERSION                  	long_name         Instrument version     
_FillValue                     8   WMO_INST_TYPE                     	long_name         Coded instrument type      conventions       Argo reference table 8     
_FillValue                    88   JULD               	long_name         ?Julian day (UTC) of the station relative to REFERENCE_DATE_TIME    standard_name         time   units         "days since 1950-01-01 00:00:00 UTC     conventions       8Relative julian days with decimal part (as parts of day)   
_FillValue        A.�~       axis      T           8@   JULD_QC                	long_name         Quality on Date and Time   conventions       Argo reference table 2     
_FillValue                    8P   JULD_LOCATION                  	long_name         @Julian day (UTC) of the location relative to REFERENCE_DATE_TIME   units         "days since 1950-01-01 00:00:00 UTC     conventions       8Relative julian days with decimal part (as parts of day)   
_FillValue        A.�~            8T   LATITUDE            	   	long_name         &Latitude of the station, best estimate     standard_name         latitude   units         degree_north   
_FillValue        @�i�       	valid_min         �V�        	valid_max         @V�        axis      Y      	reference         WGS84      coordinate_reference_frame        urn:ogc:crs:EPSG::4326          8d   	LONGITUDE               	   	long_name         'Longitude of the station, best estimate    standard_name         	longitude      units         degree_east    
_FillValue        @�i�       	valid_min         �f�        	valid_max         @f�        axis      X      	reference         WGS84      coordinate_reference_frame        urn:ogc:crs:EPSG::4326          8t   POSITION_QC                	long_name         ,Quality on position (latitude and longitude)   conventions       Argo reference table 2     
_FillValue                    8�   POSITIONING_SYSTEM                    	long_name         Positioning system     
_FillValue                    8�   PROFILE_PRES_QC                	long_name         #Global quality flag of PRES profile    conventions       Argo reference table 2a    
_FillValue                    8�   PROFILE_PSAL_QC                	long_name         #Global quality flag of PSAL profile    conventions       Argo reference table 2a    
_FillValue                    8�   PROFILE_TEMP_QC                	long_name         #Global quality flag of TEMP profile    conventions       Argo reference table 2a    
_FillValue                    8�   VERTICAL_SAMPLING_SCHEME                  	long_name         Vertical sampling scheme   conventions       Argo reference table 16    
_FillValue                    8�   CONFIG_MISSION_NUMBER                  	long_name         'Float's mission number for each profile    conventions       @0..N, 0 : launch mission (if exists), 1 : first complete mission   
_FillValue         ��        :�   PRES         
         	long_name         SEA PRESSURE   standard_name         sea_water_pressure     
_FillValue        G�O�   units         decibar    	valid_min                	valid_max         F;�    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =���   axis      Z      coordinate_reference_frame        urn:ogc:crs:EPSG::5113       P  :�   PRES_QC          
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                 �  Y�   PRES_ADJUSTED            
      	   	long_name         SEA PRESSURE   standard_name         sea_water_pressure     
_FillValue        G�O�   units         decibar    	valid_min                	valid_max         F;�    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =���     P  a�   PRES_ADJUSTED_QC         
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                 �  �    PRES_ADJUSTED_ERROR          
         	long_name         SEA PRESSURE   
_FillValue        G�O�   units         decibar    C_format      %7.1f      FORTRAN_format        F7.1   
resolution        =���     P  ��   PSAL         
      	   	long_name         PRACTICAL SALINITY     standard_name         sea_water_salinity     
_FillValue        G�O�   units         psu    	valid_min                	valid_max         B(     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     P  �D   PSAL_QC          
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                 �  ǔ   PSAL_ADJUSTED            
      	   	long_name         PRACTICAL SALINITY     standard_name         sea_water_salinity     
_FillValue        G�O�   units         psu    	valid_min                	valid_max         B(     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     P  �h   PSAL_ADJUSTED_QC         
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                 �  �   PSAL_ADJUSTED_ERROR          
         	long_name         PRACTICAL SALINITY     
_FillValue        G�O�   units         psu    C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     P  ��   TEMP         
      	   	long_name         $SEA TEMPERATURE IN SITU ITS-90 SCALE   standard_name         sea_water_temperature      
_FillValue        G�O�   units         degree_Celsius     	valid_min         �      	valid_max         B      C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     P �   TEMP_QC          
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                 � 5,   TEMP_ADJUSTED            
      	   	long_name         $SEA TEMPERATURE IN SITU ITS-90 SCALE   standard_name         sea_water_temperature      
_FillValue        G�O�   units         degree_Celsius     	valid_min         �      	valid_max         B      C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     P =    TEMP_ADJUSTED_QC         
         	long_name         quality flag   conventions       Argo reference table 2     
_FillValue                 � \P   TEMP_ADJUSTED_ERROR          
         	long_name         $SEA TEMPERATURE IN SITU ITS-90 SCALE   
_FillValue        G�O�   units         degree_Celsius     C_format      %9.3f      FORTRAN_format        F9.3   
resolution        :�o     P d$   	PARAMETER               	            	long_name         /List of parameters with calibration information    conventions       Argo reference table 3     
_FillValue                  ` �t   SCIENTIFIC_CALIB_EQUATION               	            	long_name         'Calibration equation for this parameter    
_FillValue                   ��   SCIENTIFIC_CALIB_COEFFICIENT            	            	long_name         *Calibration coefficients for this equation     
_FillValue                   ��   SCIENTIFIC_CALIB_COMMENT            	            	long_name         .Comment applying to this parameter calibration     
_FillValue                   ��   SCIENTIFIC_CALIB_DATE               	             	long_name         Date of calibration    
_FillValue                  T ��   HISTORY_INSTITUTION                      	long_name         "Institution which performed action     conventions       Argo reference table 4     
_FillValue                   �(   HISTORY_STEP                     	long_name         Step in data processing    conventions       Argo reference table 12    
_FillValue                   �0   HISTORY_SOFTWARE                     	long_name         'Name of software which performed action    conventions       Institution dependent      
_FillValue                   �8   HISTORY_SOFTWARE_RELEASE                     	long_name         2Version/release of software which performed action     conventions       Institution dependent      
_FillValue                   �@   HISTORY_REFERENCE                        	long_name         Reference of database      conventions       Institution dependent      
_FillValue                  � �H   HISTORY_DATE                      	long_name         #Date the history record was created    conventions       YYYYMMDDHHMISS     
_FillValue                   ��   HISTORY_ACTION                       	long_name         Action performed on data   conventions       Argo reference table 7     
_FillValue                   ��   HISTORY_PARAMETER                        	long_name         (Station parameter action is performed on   conventions       Argo reference table 3     
_FillValue                    ��   HISTORY_START_PRES                    	long_name          Start pressure action applied on   
_FillValue        G�O�   units         decibar        �   HISTORY_STOP_PRES                     	long_name         Stop pressure action applied on    
_FillValue        G�O�   units         decibar        �   HISTORY_PREVIOUS_VALUE                    	long_name         +Parameter/Flag previous value before action    
_FillValue        G�O�       �   HISTORY_QCTEST                       	long_name         <Documentation of tests performed, tests failed (in hex form)   conventions       EWrite tests performed when ACTION=QCP$; tests failed when ACTION=QCF$      
_FillValue                    �$Argo profile    3.0 1.2 19500101000000  20150706192058  20150706192058  4901664 4901664 US ARGO PROJECT                                                 US ARGO PROJECT                                                 Gregory C. Johnson                                              Gregory C. Johnson                                              PSAL            PRES            TEMP            PSAL            PRES            TEMP                  AA  AOAO40351692                        40440329                        2B  2B  AA                                                                  NAVISIR_SBE_0442NAVISIR_SBE_0442                                863 863 @�X��β@�[Z=�11  @�X��β@�[Z=�@Fi�����@FrM����_z��`A��_mp��
>11  GPS     GPS     AA  AA  AA  Primary sampling: averaged []                                                                                                                                                                                                                                   Primary sampling: averaged []                                                                                                                                                                                                                                         @�ff@�  A   A   AA��Aa��A~ffA�  A�  A�  A�  A�  A�  A�  B   B  B  B  B   B(  B0  B8  B@  BH  BP  BX  B`  Bh  Bp  Bx  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�33B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  C   C  C  C  C  C
  C  C  C  C  C  C  C  C  C  C  C   C"  C$  C&  C(  C*  C,  C.  C0  C2  C4  C6  C8  C:  C<  C>  C@  CB  CD  CF  CH  CJ  CL  CN�CP  CR  CT  CV  CX  CZ  C\  C^  C`  Cb  Cd  Cf  Ch  Cj  Cl  Cn  Cp  Cr  Ct  Cv  Cx  Cz  C|  C~  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  D   D � D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D	  D	� D
  D
� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D   D � D!  D!� D"  D"� D#  D#� D$  D$� D%  D%� D&  D&� D'  D'� D(  D(� D)  D)� D*  D*� D+  D+� D,  D,� D-  D-� D.  D.� D/  D/� D0  D0� D1  D1� D2  D2� D3  D3� D4  D4� D5  D5� D6  D6� D7  D7� D8  D8� D9  D9� D:  D:� D;  D;� D<  D<� D=  D=� D>  D>� D?  D?� D@  D@� DA  DA� DB  DB� DC  DC� DD  DD� DE  DE� DF  DF� DG  DG�fDH  DH� DI  DI� DJ  DJ� DK  DK� DL  DL� DM  DM� DN  DN� DO  DO� DP  DP� DQ  DQ� DR  DR� DS  DS� DT  DT� DU  DU� DV  DV� DW  DW� DX  DX� DY  DY� DZ  DZ� D[  D[� D\  D\� D]  D]� D^  D^� D_  D_� D`  D`� Da  Da�fDb  Db� Dc  Dc� Dd  Dd� De  De� Df  Df� Dg  Dg� Dh  Dh� Di  Di� Dj  Dj� Dk  Dk� Dl  Dl� Dm  Dm� Dn  Dn� Do  Do� Dp  Dp� Dq  Dq� Dr  Dr� Ds  Ds� Dt  Dt� Du  Du� Dv  Dv� Dw  Dw� Dx  Dx� Dy  Dy� Dz  Dz� D{  D{� D|  D|� D}  D}� D~  D~� D  D� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D D��3D�  D�@ DÀ D�� D�  D�@ DĀ D�� D�  D�@ Dŀ D�� D�  D�@ Dƀ D�� D�  D�@ Dǀ D�� D�  D�@ DȀ D�� D�  D�@ Dɀ D�� D�  D�@ Dʀ D�� D�  D�@ Dˀ D�� D�  D�@ D̀ D�� D�  D�@ D̀ D�� D�  D�@ D΀ D�� D�  D�@ Dπ D�� D�  D�@ DЀ D�� D�  D�@ Dр D�� D�  D�@ DҀ D�� D�  D�@ DӀ D�� D�  D�@ DԀ D�� D�  D�@ DՀ D�� D�  D�@ Dր D�� D�  D�@ D׀ D�� D�  D�@ D؀ D�� D�  D�<�Dـ D�� D�  D�@ Dڀ D�� D�  D�@ Dۀ D�� D�  D�@ D܀ D�� D�  D�@ D݀ D�� D�  D�@ Dހ D�� D�  D�@ D߀ D�� D�  D�@ D�� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D�� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D��3D�� @�33@�  A��A   A>ffA`  A�  A�  A���A�  A�33A�33A�  A�  B   B  B  B  B   B(  B0  B8  B@  BH  BP  BX  B`  Bh  Bp  Bx  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�33B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  B�  C   C  C  C  C  C
  C  C  C  C  C  C  C  C  C  C  C   C"  C$  C&  C(  C*  C,  C.  C0  C2  C4  C6  C8  C:  C<  C>  C@  CB  CD  CF  CH  CJ  CL  CN  CP  CR  CT  CV  CX  CZ  C\  C^  C`  Cb  Cd  Cf  Ch  Cj  Cl  Cn  Cp  Cr  Ct  Cv  Cx  Cz  C|  C~  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  C�  D   D � D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D	  D	� D
  D
� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D  D� D   D � D!  D!� D"  D"� D#  D#� D$  D$� D%  D%� D&  D&� D'  D'� D(  D(� D)  D)� D*  D*� D+  D+� D,  D,� D-  D-� D.  D.� D/  D/� D0  D0� D1  D1� D2  D2� D3  D3� D4  D4� D5  D5� D6  D6� D7  D7� D8  D8� D9  D9� D:  D:� D;  D;� D<  D<� D=  D=� D>  D>� D?  D?� D@  D@� DA  DA� DB  DB� DC  DC� DD  DD� DE  DE� DF  DF� DG  DG� DH  DH� DI  DI� DJ  DJ� DK  DK� DL  DL� DM  DM� DN  DN� DO  DO� DP  DP� DP��DQ� DR  DR� DS  DS� DT  DT� DU  DU� DV  DV� DW  DW� DX  DX� DY  DY� DZ  DZ� D[  D[� D\  D\� D]  D]� D^  D^� D_  D_� D`  D`� Da  Da� Db  Db� Dc  Dc� Dd  Dd� De  De� Df  Df� Dg  Dg� Dh  Dh� Di  Di� Dj  Dj� Dk  Dk� Dl  Dl� Dm  Dm� Dn  Dn� Do  Do� Dp  Dp� Dq  Dq� Dr  Dr� Ds  Ds� Dt  Dt� Du  Du� Dv  Dv� Dw  Dw� Dx  Dx� Dy  Dy� Dz  Dz� D{  D{� D|  D|� D}  D}� D~  D~� D  D� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D��3D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D D�� D�  D�@ DÀ D�� D�  D�@ DĀ D�� D�  D�@ Dŀ D�� D�  D�@ Dƀ D�� D�  D�@ Dǀ D�� D�  D�@ DȀ D�� D�  D�@ Dɀ D�� D�  D�@ Dʀ D�� D�  D�@ Dˀ D�� D�  D�@ D̀ D�� D�  D�@ D̀ D�� D�  D�@ D΀ D�� D�  D�@ Dπ D�� D�  D�@ DЀ D�� D�  D�@ Dр D�� D�  D�@ DҀ D�� D�  D�@ DӀ D�� D�  D�@ DԀ D�� D�  D�@ DՀ D�� D�  D�@ Dր D�� D�  D�@ D׀ D�� D�  D�@ D؀ D�� D�  D�@ Dـ D�� D�  D�@ Dڀ D�� D�  D�@ Dۀ D�� D�  D�@ D܀ D�� D�  D�@ D݀ D�� D�  D�@ Dހ D�� D�  D�@ D߀ D�� D�  D�@ D�� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D�� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D� D�� D�  D�@ D�� D�� D�  D�@ D�� D�� D�  D�@ D��3D���G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111            @���@\AG�A!G�AB�HAb�HA�A���A���A���A���AУ�A��A��B Q�BQ�BQ�BQ�B Q�B(Q�B0Q�B8Q�B@Q�BHQ�BPQ�BXQ�B`Q�BhQ�BpQ�BxQ�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�\)B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�B�(�C {C{C{C{C{C
{C{C{C{C{C{C{C{C{C{C{C {C"{C${C&{C({C*{C,{C.{C0{C2{C4{C6{C8{C:{C<{C>{C@{CB{CD{CF{CH{CJ{CL{CN.CP{CR{CT{CV{CX{CZ{C\{C^{C`{Cb{Cd{Cf{Ch{Cj{Cl{Cn{Cp{Cr{Ct{Cv{Cx{Cz{C|{C~{C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=C�
=D D �DD�DD�DD�DD�DD�DD�DD�DD�D	D	�D
D
�DD�DD�DD�DD�DD�DD�DD�DD�DD�DD�DD�DD�DD�DD�DD�DD�DD�DD�DD�DD�DD�D D �D!D!�D"D"�D#D#�D$D$�D%D%�D&D&�D'D'�D(D(�D)D)�D*D*�D+D+�D,D,�D-D-�D.D.�D/D/�D0D0�D1D1�D2D2�D3D3�D4D4�D5D5�D6D6�D7D7�D8D8�D9D9�D:D:�D;D;�D<D<�D=D=�D>D>�D?D?�D@D@�DADA�DBDB�DCDC�DDDD�DEDE�DFDF�DGDG��DHDH�DIDI�DJDJ�DKDK�DLDL�DMDM�DNDN�DODO�DPDP�DQDQ�DRDR�DSDS�DTDT�DUDU�DVDV�DWDW�DXDX�DYDY�DZDZ�D[D[�D\D\�D]D]�D^D^�D_D_�D`D`�DaDa��DbDb�DcDc�DdDd�DeDe�DfDf�DgDg�DhDh�DiDi�DjDj�DkDk�DlDl�DmDm�DnDn�DoDo�DpDp�DqDq�DrDr�DsDs�DtDt�DuDu�DvDv�DwDw�DxDx�DyDy�DzDz�D{D{�D|D|�D}D}�D~D~�DD�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D�D���D��D�B�DÂ�D�D��D�B�DĂ�D�D��D�B�Dł�D�D��D�B�DƂ�D�D��D�B�Dǂ�D�D��D�B�DȂ�D�D��D�B�Dɂ�D�D��D�B�Dʂ�D�D��D�B�D˂�D�D��D�B�D̂�D�D��D�B�D͂�D�D��D�B�D΂�D�D��D�B�Dς�D�D��D�B�DЂ�D�D��D�B�Dт�D�D��D�B�D҂�D�D��D�B�Dӂ�D�D��D�B�DԂ�D�D��D�B�DՂ�D�D��D�B�Dւ�D�D��D�B�Dׂ�D�D��D�B�D؂�D�D��D�?\Dق�D�D��D�B�Dڂ�D�D��D�B�Dۂ�D�D��D�B�D܂�D�D��D�B�D݂�D�D��D�B�Dނ�D�D��D�B�D߂�D�D��D�B�D���D�D��D�B�DႏD�D��D�B�D₏D�D��D�B�DわD�D��D�B�D䂏D�D��D�B�D傏D�D��D�B�D悏D�D��D�B�D炏D�D��D�B�D肏D�D��D�B�D邏D�D��D�B�DꂏD�D��D�B�D낏D�D��D�B�D삏D�D��D�B�D킏D�D��D�B�DD�D��D�B�DD�D��D�B�D���D�D��D�B�D�D�D��D�B�D�D�D��D�B�D�D�D��D�B�D�D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�D��D�B�D���D�@�Q�@��A(�A"�\A@��Ab�\A�G�A�G�A�{A�G�A�z�A�z�A�G�A�G�B ��B��B��B��B ��B(��B0��B8��B@��BH��BP��BX��B`��Bh��Bp��Bx��B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B��B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�B�Q�C (�C(�C(�C(�C(�C
(�C(�C(�C(�C(�C(�C(�C(�C(�C(�C(�C (�C"(�C$(�C&(�C((�C*(�C,(�C.(�C0(�C2(�C4(�C6(�C8(�C:(�C<(�C>(�C@(�CB(�CD(�CF(�CH(�CJ(�CL(�CN(�CP(�CR(�CT(�CV(�CX(�CZ(�C\(�C^(�C`(�Cb(�Cd(�Cf(�Ch(�Cj(�Cl(�Cn(�Cp(�Cr(�Ct(�Cv(�Cx(�Cz(�C|(�C~(�C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{C�{D 
=D �=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D	
=D	�=D

=D
�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D
=D�=D 
=D �=D!
=D!�=D"
=D"�=D#
=D#�=D$
=D$�=D%
=D%�=D&
=D&�=D'
=D'�=D(
=D(�=D)
=D)�=D*
=D*�=D+
=D+�=D,
=D,�=D-
=D-�=D.
=D.�=D/
=D/�=D0
=D0�=D1
=D1�=D2
=D2�=D3
=D3�=D4
=D4�=D5
=D5�=D6
=D6�=D7
=D7�=D8
=D8�=D9
=D9�=D:
=D:�=D;
=D;�=D<
=D<�=D=
=D=�=D>
=D>�=D?
=D?�=D@
=D@�=DA
=DA�=DB
=DB�=DC
=DC�=DD
=DD�=DE
=DE�=DF
=DF�=DG
=DG�=DH
=DH�=DI
=DI�=DJ
=DJ�=DK
=DK�=DL
=DL�=DM
=DM�=DN
=DN�=DO
=DO�=DP
=DP�=DQ�DQ�=DR
=DR�=DS
=DS�=DT
=DT�=DU
=DU�=DV
=DV�=DW
=DW�=DX
=DX�=DY
=DY�=DZ
=DZ�=D[
=D[�=D\
=D\�=D]
=D]�=D^
=D^�=D_
=D_�=D`
=D`�=Da
=Da�=Db
=Db�=Dc
=Dc�=Dd
=Dd�=De
=De�=Df
=Df�=Dg
=Dg�=Dh
=Dh�=Di
=Di�=Dj
=Dj�=Dk
=Dk�=Dl
=Dl�=Dm
=Dm�=Dn
=Dn�=Do
=Do�=Dp
=Dp�=Dq
=Dq�=Dr
=Dr�=Ds
=Ds�=Dt
=Dt�=Du
=Du�=Dv
=Dv�=Dw
=Dw�=Dx
=Dx�=Dy
=Dy�=Dz
=Dz�=D{
=D{�=D|
=D|�=D}
=D}�=D~
=D~�=D
=D�=D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��RD��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�ED��D��D�D�EDD��D�D�EDÅD��D�D�EDąD��D�D�EDŅD��D�D�EDƅD��D�D�EDǅD��D�D�EDȅD��D�D�EDɅD��D�D�EDʅD��D�D�ED˅D��D�D�ED̅D��D�D�EDͅD��D�D�ED΅D��D�D�EDυD��D�D�EDЅD��D�D�EDхD��D�D�ED҅D��D�D�EDӅD��D�D�EDԅD��D�D�EDՅD��D�D�EDօD��D�D�EDׅD��D�D�ED؅D��D�D�EDمD��D�D�EDڅD��D�D�EDۅD��D�D�ED܅D��D�D�ED݅D��D�D�EDޅD��D�D�ED߅D��D�D�ED��D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED��D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED�D��D�D�ED��D��D�D�ED��D��D�D�ED��RD���G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111            G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�A��A��A��A��A��A��RA�n�B k�B ��B B ��BuB\)Bz�B� B�B�B�B}�B}�B}�B� B�%B�JB�\B�hB�uB��B��B��B�B�RB��B��B��B�B�HB�B
=BuB'�B@�B� B��B�B��B��B49BW
Bo�B��B��B��B�B33B?}B@�BXBjB�B��B��B�yB��BVB'�BI�B_;BjB{�B��B��B�dB��B�
B�;B�BPB;dBL�BI�BZBk�B�%B��B��B��B��B�B�NB�B��BB�B �B&�B-B1'B;dBE�BT�B\)B^5BaHBffBk�Br�Bw�B~�B� B�B�=B�PB�\B�oB�oB��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B�!B�XB�RB�LB�}B�RB�FB�XB�wBŢB�
B�B�B�B�B�B�B�B��B��B��B��B�B�B�B�B�B�B�B�B��B��B��B�B�/B�B��B��B��B��B��B��B��B��B��B��B�B�/B�mB�B�B�mB�yB�B�B�B��B��B��B��B��B��BB+B1B1B1B
=BVB\B\B\B{BoBbBJBPBVB\BhBoBuB�B�B�B!�B&�B+B+B+B.B-B/B1'B1'B49B7LB9XB:^B:^B;dB>wB@�BB�BB�BA�BB�BB�BC�BF�BK�BN�BL�BK�BO�BO�BQ�BQ�BW
BW
BXBYBZB\)B]/B_;BcTBffBhsBjBl�Bn�Bn�Bp�Bp�Bq�Bt�Bu�Bu�Bv�Bw�By�Bz�B|�B~�B� B}�B}�B� B�B�%B�+B�=B�VB�hB�hB�uB��B��B��B��B��B��B��B��B��B��B��B��B��B�B�B�!B�'B�9B�?B�FB�LB�^B�jB�}B��B��BÖBǮBȴB��B��B��B��B��B�B�B�B�#B�/B�;B�HB�HB�NB�NB�ZB�fB�mB�yB�B�B�B�B�B�B��B��B��B��B��B��B��B��B	  B	  B	B	B	B	B	B	B	B	%B	%B	1B	1B	1B	
=B	PB	VB	\B	\B	bB	bB	bB	bB	bB	hB	uB	{B	�B	�B	�B	�B	�B	�B	 �B	"�B	#�B	&�B	'�B	)�B	+B	,B	,B	-B	/B	2-B	5?B	6FB	7LB	8RB	9XB	:^B	:^B	;dB	;dB	<jB	<jB	>wB	?}B	@�B	@�B	A�B	A�B	C�B	D�B	E�B	F�B	F�B	G�B	I�B	I�B	J�B	J�B	J�B	K�B	L�B	N�B	O�B	P�B	Q�B	R�B	S�B	T�B	VB	VB	W
B	W
B	YB	ZB	\)B	]/B	^5B	_;B	aHB	bNB	bNB	bNB	bNB	cTB	dZB	ffB	gmB	hsB	iyB	iyB	jB	k�B	m�B	n�B	o�B	o�B	p�B	p�B	r�B	s�B	u�B	w�B	y�B	z�B	{�B	|�B	|�B	}�B	}�B	� B	�B	�B	�B	�B	�B	�%B	�+B	�+B	�+B	�+B	�1B	�1B	�=B	�=B	�=B	�JB	�PB	�VB	�VB	�\B	�bB	�bB	�bB	�hB	�oB	�{B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�!B	�!B	�'B	�'B	�-B	�3B	�3B	�9B	�?B	�?B	�?B	�LB	�LB	�RB	�RB	�XB	�^B	�^B	�dB	�dB	�dB	�dB	�dB	�dB	�jB	�qB	�wB	�wB	��B	��B	��B	��B	��B	��B	B	ĜB	ǮB	ǮB	ǮB	ȴB	ȴB	ɺB	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	�B	�
B	�
B	�B	�B	�B	�B	�B	�B	�B	�#B	�#B	�)B	�)B	�)B	�/B	�/B	�/B	�/B	�5B	�5B	�BB	�HB	�NB	�NB	�NB	�NB	�NB	�NB	�TB	�ZB	�`B	�`B	�`B	�`B	�`B	�`B	�`B	�`B	�fB	�mB	�sB	�sB	�sB	�sB	�sB	�sB	�yB	�yB	�yB	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B
  B
  B
  B
B
B
B
B
B
B
B
B
B
B
%B
+B
1B
	7B
	7B
	7B
	7B
	7B
	7B
	7B
	7B

=B

=B
DB
JB
JB
JB
VB
VB
\B
\B
bB
bB
bB
hB
hB
oB
uB
uB
uB
uB
{B
uB
{B
{B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
 �B
 �B
 �B
!�B
!�B
"�B
"�B
#�B
#�B
#�B
#�B
$�B
$�B
$�B
%�B
%�B
&�B
'�B
'�B
'�B
(�B
(�B
(�B
)�B
)�B
)�B
)�B
+B
+B
,B
,B
,B
,B
-B
.B
.B
/B
/B
/B
0!B
0!B
0!B
1'B
1'B
1'B
2-B
2-B
2-B
33B
33B
49B
49B
49B
49B
5?B
5?B
5?B
6FB
6FB
6FB
6FB
6FB
7LB
7LB
8RB
8RB
8RB
8RB
8RB
8RB
9XB
9XB
:^B
;dB
;dB
;dB
<jB
<jB
=qB
=qB
>wB
?}B
?}B
@�B
@�B
@�B
A�B
A�B
A�B
B�B
B�B
C�B
C�B
C�B
D�B
D�B
E�B
E�B
E�B
E�B
E�B
F�B
F�B
F�B
F�B
G�B
G�B
H�B
H�B
H�B
H�B
I�B
I�B
I�B
J�B
J�B
J�B
K�B
K�B
L�B
M�B
N�B
N�B
N�B
N�B
N�B
O�B
O�B
O�B
P�B
P�B
P�B
Q�B
Q�B
Q�B
Q�B
R�B
R�B
S�B
T�B
T�B
VB
VB
VB
VB
W
B
W
B
W
B
W
B
W
B
XB
YB
ZB
ZB
ZB
ZB
[#B
[#B
[#B
[#B
[#B
\)B
\)B
]/B
]/B
]/B
]/B
]/B
]/B
]/B
^5B
^5B
_;B
_;B
`BB
`BA�dZA��FA���A���A��A��TA��;A��`A�bNA�oA��A�r�B cTB&�B>wBZBhsBv�B~�B�B�B�B�%B�1B�bB�{B�hB��B��B��B�B�^BȴB�HB+BPB.B?}BdZB�B�{B�jB��BBoB?}B\)B}�B��B�LB��B��B�B!�BJ�B_;Br�B��B��B�mBB�BC�BaHB� B��B��B�}B��B��B  B�B"�BG�B_;Bm�Br�By�B�PB��B��B�3B�^B�}BŢB��B�TB�B��BBPB�B �B!�B#�B#�B$�B%�B(�B/B:^BE�BVB_;Bk�Br�Bs�Bs�Bw�B~�B�1B�1B�\B�uB��B��B��B��B��B��B��B�B��B��B��B��B��B��B��B�B�B�B�'B�FB�RB�dBBƨBɺB��B��BȴBɺB��B��B��B�B�
B�
B�B�
B�)B�;B�;B�#B�B�B�/B�HB�5B�B�B�#B�/B�/B�ZB�fB�/B�
B��B��B��B�B�/B�;B�5B�;B�NB�fB�yB�B�B�B�B�B��B��B�B�B��B��BBbB{B�B�B�B�B�B�B�B!�B"�B!�B!�B!�B"�B#�B&�B'�B)�B'�B#�B$�B(�B)�B+B,B-B,B/B0!B1'B2-B33B5?B7LB8RB=qB@�BA�BB�BC�BE�BF�BG�BG�BI�BI�BI�BI�BJ�BK�BL�BM�BN�BO�BO�BP�BS�BT�BT�BW
BXBYB[#B[#B\)B^5B_;B^5B`BBaHBbNBe`Bk�Bm�Bp�Bs�Bs�Bs�Bu�Bx�By�By�B{�B~�B� B� B�B�B�B�%B�+B�=B�JB�VB�bB�oB�{B��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B�B�B�B�B�!B�9B�FB�LB�RB�XB�^B�dB�jB�wB��BÖBŢBŢBƨBǮBȴBɺB��B��B��B��B��B��B��B��B��B�B�
B�B�#B�#B�)B�HB�NB�NB�TB�`B�fB�mB�sB�yB�yB�B�B�B�B�B�B�B�B�B��B��B��B��B��B��B��B��B��B	B	B	B	B	+B	+B	1B	1B	
=B	DB	PB	VB	\B	bB	oB	uB	�B	�B	�B	�B	�B	�B	�B	 �B	 �B	!�B	"�B	$�B	%�B	'�B	)�B	,B	.B	0!B	2-B	2-B	49B	6FB	7LB	9XB	9XB	:^B	;dB	;dB	<jB	>wB	?}B	@�B	A�B	A�B	B�B	B�B	C�B	E�B	F�B	I�B	I�B	J�B	L�B	L�B	M�B	N�B	P�B	R�B	S�B	VB	W
B	XB	XB	YB	ZB	]/B	^5B	^5B	_;B	_;B	`BB	`BB	aHB	aHB	bNB	cTB	e`B	ffB	hsB	jB	jB	k�B	l�B	m�B	n�B	n�B	p�B	p�B	q�B	q�B	r�B	s�B	t�B	u�B	v�B	w�B	x�B	y�B	{�B	|�B	}�B	~�B	� B	� B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�%B	�%B	�+B	�1B	�7B	�JB	�PB	�PB	�VB	�VB	�\B	�\B	�\B	�bB	�hB	�uB	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�!B	�!B	�!B	�'B	�'B	�-B	�9B	�FB	�FB	�LB	�XB	�XB	�^B	�dB	�jB	�qB	�wB	�wB	�wB	�}B	�}B	��B	��B	��B	��B	B	ÖB	ÖB	ÖB	ĜB	ĜB	ĜB	ĜB	ŢB	ƨB	ǮB	ȴB	ȴB	ȴB	ɺB	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	�B	�B	�B	�
B	�
B	�B	�B	�B	�B	�B	�B	�B	�B	�#B	�#B	�#B	�#B	�)B	�)B	�/B	�5B	�5B	�5B	�5B	�5B	�5B	�/B	�5B	�;B	�;B	�;B	�;B	�5B	�5B	�;B	�/B	�)B	�/B	�5B	�BB	�BB	�TB	�TB	�TB	�TB	�NB	�HB	�HB	�HB	�HB	�NB	�TB	�ZB	�ZB	�ZB	�`B	�`B	�`B	�`B	�fB	�mB	�fB	�`B	�`B	�`B	�`B	�`B	�fB	�mB	�sB	�yB	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B
  B
  B
  B
B
B
B
B
B
B
%B
+B
+B
1B
	7B
	7B
DB
DB
DB
JB
PB
PB
PB
VB
VB
VB
\B
\B
\B
\B
bB
bB
hB
hB
hB
hB
hB
oB
oB
oB
oB
oB
uB
uB
uB
uB
uB
uB
uB
uB
uB
uB
{B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
!�B
#�B
#�B
$�B
$�B
$�B
$�B
&�B
'�B
'�B
'�B
(�B
(�B
(�B
(�B
)�B
)�B
+B
+B
+B
,B
,B
-B
-B
-B
.B
.B
/B
/B
/B
/B
/B
0!B
0!B
0!B
1'B
1'B
1'B
2-B
2-B
2-B
33B
33B
33B
33B
49B
5?B
5?B
5?B
5?B
5?B
6FB
6FB
7LB
7LB
7LB
7LB
8RB
8RB
8RB
8RB
8RB
9XB
9XB
9XB
:^B
:^B
;dB
;dB
;dB
;dB
;dB
<jB
<jB
<jB
<jB
=qB
=qB
=qB
=qB
>wB
>wB
>wB
?}B
?}B
?}B
?}B
?}B
?}B
?}B
@�B
@�B
@�B
@�B
A�B
A�B
A�B
B�B
B�B
B�B
B�B
C�B
C�B
C�B
D�B
D�B
E�B
F�B
F�B
G�B
G�B
G�B
G�B
H�B
H�B
I�B
I�B
J�B
J�B
J�B
J�B
J�B
J�B
K�B
K�B
K�B
L�B
L�B
L�B
M�B
M�B
M�B
M�B
N�B
N�B
O�B
O�B
P�B
P�B
P�B
Q�B
Q�B
Q�B
Q�B
Q�B
R�B
R�B
R�B
R�B
R�B
S�B
S�B
S�B
T�B
T�B
T�B
VB
VB
VB
VB
W
B
W
B
W
B
W
B
XB
XB
XB
XB
XB
YB
YB
YB
ZB
ZB
ZB
ZB
ZB
[#B
[#B
\)B
\)B
\)B
\)B
]/B
]/B
^5B
^5G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111            A��A��A��A��A��A��RA�n�B k�B ��B B ��BuB\)Bz�B� B�B�B�B}�B}�B}�B� B�%B�JB�\B�hB�uB��B��B��B�B�RB��B��B��B�B�HB�B
=BuB'�B@�B� B��B�B��B��B49BW
Bo�B��B��B��B�B33B?}B@�BXBjB�B��B��B�yB��BVB'�BI�B_;BjB{�B��B��B�dB��B�
B�;B�BPB;dBL�BI�BZBk�B�%B��B��B��B��B�B�NB�B��BB�B �B&�B-B1'B;dBE�BT�B\)B^5BaHBffBk�Br�Bw�B~�B� B�B�=B�PB�\B�oB�oB��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B�!B�XB�RB�LB�}B�RB�FB�XB�wBŢB�
B�B�B�B�B�B�B�B��B��B��B��B�B�B�B�B�B�B�B�B��B��B��B�B�/B�B��B��B��B��B��B��B��B��B��B��B�B�/B�mB�B�B�mB�yB�B�B�B��B��B��B��B��B��BB+B1B1B1B
=BVB\B\B\B{BoBbBJBPBVB\BhBoBuB�B�B�B!�B&�B+B+B+B.B-B/B1'B1'B49B7LB9XB:^B:^B;dB>wB@�BB�BB�BA�BB�BB�BC�BF�BK�BN�BL�BK�BO�BO�BQ�BQ�BW
BW
BXBYBZB\)B]/B_;BcTBffBhsBjBl�Bn�Bn�Bp�Bp�Bq�Bt�Bu�Bu�Bv�Bw�By�Bz�B|�B~�B� B}�B}�B� B�B�%B�+B�=B�VB�hB�hB�uB��B��B��B��B��B��B��B��B��B��B��B��B��B�B�B�!B�'B�9B�?B�FB�LB�^B�jB�}B��B��BÖBǮBȴB��B��B��B��B��B�B�B�B�#B�/B�;B�HB�HB�NB�NB�ZB�fB�mB�yB�B�B�B�B�B�B��B��B��B��B��B��B��B��B	  B	  B	B	B	B	B	B	B	B	%B	%B	1B	1B	1B	
=B	PB	VB	\B	\B	bB	bB	bB	bB	bB	hB	uB	{B	�B	�B	�B	�B	�B	�B	 �B	"�B	#�B	&�B	'�B	)�B	+B	,B	,B	-B	/B	2-B	5?B	6FB	7LB	8RB	9XB	:^B	:^B	;dB	;dB	<jB	<jB	>wB	?}B	@�B	@�B	A�B	A�B	C�B	D�B	E�B	F�B	F�B	G�B	I�B	I�B	J�B	J�B	J�B	K�B	L�B	N�B	O�B	P�B	Q�B	R�B	S�B	T�B	VB	VB	W
B	W
B	YB	ZB	\)B	]/B	^5B	_;B	aHB	bNB	bNB	bNB	bNB	cTB	dZB	ffB	gmB	hsB	iyB	iyB	jB	k�B	m�B	n�B	o�B	o�B	p�B	p�B	r�B	s�B	u�B	w�B	y�B	z�B	{�B	|�B	|�B	}�B	}�B	� B	�B	�B	�B	�B	�B	�%B	�+B	�+B	�+B	�+B	�1B	�1B	�=B	�=B	�=B	�JB	�PB	�VB	�VB	�\B	�bB	�bB	�bB	�hB	�oB	�{B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�!B	�!B	�'B	�'B	�-B	�3B	�3B	�9B	�?B	�?B	�?B	�LB	�LB	�RB	�RB	�XB	�^B	�^B	�dB	�dB	�dB	�dB	�dB	�dB	�jB	�qB	�wB	�wB	��B	��B	��B	��B	��B	��B	B	ĜB	ǮB	ǮB	ǮB	ȴB	ȴB	ɺB	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	�B	�
B	�
B	�B	�B	�B	�B	�B	�B	�B	�#B	�#B	�)B	�)B	�)B	�/B	�/B	�/B	�/B	�5B	�5B	�BB	�HB	�NB	�NB	�NB	�NB	�NB	�NB	�TB	�ZB	�`B	�`B	�`B	�`B	�`B	�`B	�`B	�`B	�fB	�mB	�sB	�sB	�sB	�sB	�sB	�sB	�yB	�yB	�yB	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B
  B
  B
  B
B
B
B
B
B
B
B
B
B
B
%B
+B
1B
	7B
	7B
	7B
	7B
	7B
	7B
	7B
	7B

=B

=B
DB
JB
JB
JB
VB
VB
\B
\B
bB
bB
bB
hB
hB
oB
uB
uB
uB
uB
{B
uB
{B
{B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
 �B
 �B
 �B
!�B
!�B
"�B
"�B
#�B
#�B
#�B
#�B
$�B
$�B
$�B
%�B
%�B
&�B
'�B
'�B
'�B
(�B
(�B
(�B
)�B
)�B
)�B
)�B
+B
+B
,B
,B
,B
,B
-B
.B
.B
/B
/B
/B
0!B
0!B
0!B
1'B
1'B
1'B
2-B
2-B
2-B
33B
33B
49B
49B
49B
49B
5?B
5?B
5?B
6FB
6FB
6FB
6FB
6FB
7LB
7LB
8RB
8RB
8RB
8RB
8RB
8RB
9XB
9XB
:^B
;dB
;dB
;dB
<jB
<jB
=qB
=qB
>wB
?}B
?}B
@�B
@�B
@�B
A�B
A�B
A�B
B�B
B�B
C�B
C�B
C�B
D�B
D�B
E�B
E�B
E�B
E�B
E�B
F�B
F�B
F�B
F�B
G�B
G�B
H�B
H�B
H�B
H�B
I�B
I�B
I�B
J�B
J�B
J�B
K�B
K�B
L�B
M�B
N�B
N�B
N�B
N�B
N�B
O�B
O�B
O�B
P�B
P�B
P�B
Q�B
Q�B
Q�B
Q�B
R�B
R�B
S�B
T�B
T�B
VB
VB
VB
VB
W
B
W
B
W
B
W
B
W
B
XB
YB
ZB
ZB
ZB
ZB
[#B
[#B
[#B
[#B
[#B
\)B
\)B
]/B
]/B
]/B
]/B
]/B
]/B
]/B
^5B
^5B
_;B
_;B
`BB
`BA�dZA��FA���A���A��A��TA��;A��`A�bNA�oA��A�r�B cTB&�B>wBZBhsBv�B~�B�B�B�B�%B�1B�bB�{B�hB��B��B��B�B�^BȴB�HB+BPB.B?}BdZB�B�{B�jB��BBoB?}B\)B}�B��B�LB��B��B�B!�BJ�B_;Br�B��B��B�mBB�BC�BaHB� B��B��B�}B��B��B  B�B"�BG�B_;Bm�Br�By�B�PB��B��B�3B�^B�}BŢB��B�TB�B��BBPB�B �B!�B#�B#�B$�B%�B(�B/B:^BE�BVB_;Bk�Br�Bs�Bs�Bw�B~�B�1B�1B�\B�uB��B��B��B��B��B��B��B�B��B��B��B��B��B��B��B�B�B�B�'B�FB�RB�dBBƨBɺB��B��BȴBɺB��B��B��B�B�
B�
B�B�
B�)B�;B�;B�#B�B�B�/B�HB�5B�B�B�#B�/B�/B�ZB�fB�/B�
B��B��B��B�B�/B�;B�5B�;B�NB�fB�yB�B�B�B�B�B��B��B�B�B��B��BBbB{B�B�B�B�B�B�B�B!�B"�B!�B!�B!�B"�B#�B&�B'�B)�B'�B#�B$�B(�B)�B+B,B-B,B/B0!B1'B2-B33B5?B7LB8RB=qB@�BA�BB�BC�BE�BF�BG�BG�BI�BI�BI�BI�BJ�BK�BL�BM�BN�BO�BO�BP�BS�BT�BT�BW
BXBYB[#B[#B\)B^5B_;B^5B`BBaHBbNBe`Bk�Bm�Bp�Bs�Bs�Bs�Bu�Bx�By�By�B{�B~�B� B� B�B�B�B�%B�+B�=B�JB�VB�bB�oB�{B��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B��B�B�B�B�B�!B�9B�FB�LB�RB�XB�^B�dB�jB�wB��BÖBŢBŢBƨBǮBȴBɺB��B��B��B��B��B��B��B��B��B�B�
B�B�#B�#B�)B�HB�NB�NB�TB�`B�fB�mB�sB�yB�yB�B�B�B�B�B�B�B�B�B��B��B��B��B��B��B��B��B��B	B	B	B	B	+B	+B	1B	1B	
=B	DB	PB	VB	\B	bB	oB	uB	�B	�B	�B	�B	�B	�B	�B	 �B	 �B	!�B	"�B	$�B	%�B	'�B	)�B	,B	.B	0!B	2-B	2-B	49B	6FB	7LB	9XB	9XB	:^B	;dB	;dB	<jB	>wB	?}B	@�B	A�B	A�B	B�B	B�B	C�B	E�B	F�B	I�B	I�B	J�B	L�B	L�B	M�B	N�B	P�B	R�B	S�B	VB	W
B	XB	XB	YB	ZB	]/B	^5B	^5B	_;B	_;B	`BB	`BB	aHB	aHB	bNB	cTB	e`B	ffB	hsB	jB	jB	k�B	l�B	m�B	n�B	n�B	p�B	p�B	q�B	q�B	r�B	s�B	t�B	u�B	v�B	w�B	x�B	y�B	{�B	|�B	}�B	~�B	� B	� B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�%B	�%B	�+B	�1B	�7B	�JB	�PB	�PB	�VB	�VB	�\B	�\B	�\B	�bB	�hB	�uB	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�!B	�!B	�!B	�'B	�'B	�-B	�9B	�FB	�FB	�LB	�XB	�XB	�^B	�dB	�jB	�qB	�wB	�wB	�wB	�}B	�}B	��B	��B	��B	��B	B	ÖB	ÖB	ÖB	ĜB	ĜB	ĜB	ĜB	ŢB	ƨB	ǮB	ȴB	ȴB	ȴB	ɺB	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	�B	�B	�B	�
B	�
B	�B	�B	�B	�B	�B	�B	�B	�B	�#B	�#B	�#B	�#B	�)B	�)B	�/B	�5B	�5B	�5B	�5B	�5B	�5B	�/B	�5B	�;B	�;B	�;B	�;B	�5B	�5B	�;B	�/B	�)B	�/B	�5B	�BB	�BB	�TB	�TB	�TB	�TB	�NB	�HB	�HB	�HB	�HB	�NB	�TB	�ZB	�ZB	�ZB	�`B	�`B	�`B	�`B	�fB	�mB	�fB	�`B	�`B	�`B	�`B	�`B	�fB	�mB	�sB	�yB	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	�B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B	��B
  B
  B
  B
B
B
B
B
B
B
%B
+B
+B
1B
	7B
	7B
DB
DB
DB
JB
PB
PB
PB
VB
VB
VB
\B
\B
\B
\B
bB
bB
hB
hB
hB
hB
hB
oB
oB
oB
oB
oB
uB
uB
uB
uB
uB
uB
uB
uB
uB
uB
{B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
�B
!�B
#�B
#�B
$�B
$�B
$�B
$�B
&�B
'�B
'�B
'�B
(�B
(�B
(�B
(�B
)�B
)�B
+B
+B
+B
,B
,B
-B
-B
-B
.B
.B
/B
/B
/B
/B
/B
0!B
0!B
0!B
1'B
1'B
1'B
2-B
2-B
2-B
33B
33B
33B
33B
49B
5?B
5?B
5?B
5?B
5?B
6FB
6FB
7LB
7LB
7LB
7LB
8RB
8RB
8RB
8RB
8RB
9XB
9XB
9XB
:^B
:^B
;dB
;dB
;dB
;dB
;dB
<jB
<jB
<jB
<jB
=qB
=qB
=qB
=qB
>wB
>wB
>wB
?}B
?}B
?}B
?}B
?}B
?}B
?}B
@�B
@�B
@�B
@�B
A�B
A�B
A�B
B�B
B�B
B�B
B�B
C�B
C�B
C�B
D�B
D�B
E�B
F�B
F�B
G�B
G�B
G�B
G�B
H�B
H�B
I�B
I�B
J�B
J�B
J�B
J�B
J�B
J�B
K�B
K�B
K�B
L�B
L�B
L�B
M�B
M�B
M�B
M�B
N�B
N�B
O�B
O�B
P�B
P�B
P�B
Q�B
Q�B
Q�B
Q�B
Q�B
R�B
R�B
R�B
R�B
R�B
S�B
S�B
S�B
T�B
T�B
T�B
VB
VB
VB
VB
W
B
W
B
W
B
W
B
XB
XB
XB
XB
XB
YB
YB
YB
ZB
ZB
ZB
ZB
ZB
[#B
[#B
\)B
\)B
\)B
\)B
]/B
]/B
^5B
^5G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111            G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�Am�mAm�mAm�mAm�mAm�mAm�-AlAi�-Ag��Ae�^Ad��A\�AU�-AR��AQ�AP�AO+AM;dAK�AJ��AI�-AH��AG�;AF�+AE�PAEAD1AC�AB��AA��A@�jA?�#A=A=+A<ZA;�A9�A6-A3?}A2=qA/�;A,�DA&�jA#�#A"�!Ax�A��AQ�AdZA�PA  Ap�A�
A;dA	��A�AJA�+A��A�^A�
A�hAt�A33AffA��A�-A��AJA;dA�;A �9@��-@��@��9@�j@��w@���@�S�@��!@�1'@�"�@�l�@���@�?}@��@�1'@��P@�"�@�33@���@�ȴ@�=q@�?}@���@���@�z�@�1'@�|�@���@�@���@�9@�I�@�@���@��@�7L@�1@�w@�\)@�@�O�@�%@�9@�z�@�@���@�+@�=q@�@���@��
@�!@��@�Ĝ@�S�@���@��@�bN@ۅ@��@ڰ!@ڏ\@ف@�V@��#@�7L@�r�@ٺ^@���@ա�@պ^@��@���@ج@�bN@�K�@��@և+@�M�@�{@�&�@�A�@�t�@҇+@�n�@Ѳ-@�`B@�j@·+@��T@��#@�hs@�Ĝ@̋D@��@ɩ�@ʏ\@��y@�hs@���@�x�@ċD@��
@�K�@+@��h@�?}@�1@�;d@�+@��@�Z@��9@���@��@���@���@�V@��R@�+@��@���@�^5@��7@�O�@�7L@���@�bN@���@��@��\@�V@�M�@��@���@���@�dZ@�{@���@���@�|�@�\)@�33@���@��#@��-@��^@���@���@���@�x�@��`@��@�z�@���@��@�o@���@�J@��-@�X@�7L@���@�bN@�9X@��@���@��@�"�@��@�@��@�?}@�`B@�hs@���@�33@�@�@���@��h@�hs@�?}@�7L@�/@���@�r�@� �@��@��m@�\)@�+@�+@��!@�^5@�M�@�-@�@��T@��T@���@���@�hs@�V@�%@�%@�1@���@���@�@���@���@�%@���@�z�@�9X@�z�@���@�Q�@�b@�(�@�1@��w@��P@�|�@��F@�l�@�S�@��@���@���@��\@�J@��h@�O�@�Ĝ@�r�@�r�@�A�@�  @��@�t�@��@�v�@�v�@�ff@��^@�&�@���@�I�@��m@���@���@�K�@��@��@���@�~�@�-@�@�x�@�hs@�O�@�7L@���@�z�@�A�@�  @��
@�dZ@��H@���@�n�@�5?@��T@��^@�p�@�O�@�?}@�?}@��@�Ĝ@���@��D@�j@�1'@��@��;@���@��P@�|�@�S�@��@���@���@�n�@�$�@��@��#@���@�@���@���@���@���@��h@�p�@�G�@�&�@�%@���@���@���@�bN@���@��@��;@���@���@�|�@�l�@�\)@�K�@��@��H@�n�@��@���@�x�@�/@��`@���@��9@��u@�z�@�Q�@�b@���@�ƨ@���@��P@�t�@�C�@�o@���@��y@�ȴ@���@���@�n�@�5?@�{@��@��#@���@��^@��h@�/@�V@��/@���@��@�bN@�9X@�  @�@�P@\)@~��@~5?@}�-@}�@}`B@}�@|z�@|1@{�m@{�
@{ƨ@{�@{o@z�\@z=q@y�^@y�7@yhs@y&�@xĜ@xA�@w�;@w�P@wK�@w
=@v��@v��@v5?@u��@t�j@tI�@t1@s��@sdZ@s33@r��@r^5@q�#@q��@qhs@qX@p�`@p�@o�@o�P@ol�@ol�@o\)@o;d@n�y@nv�@nff@nff@m�T@m��@m`B@m�@l�D@lI�@k��@kƨ@kt�@j�H@j^5@i��@i��@ix�@iX@i�@h�u@hQ�@h �@g�@g�w@g�P@fȴ@f$�@f@f@e�@e@e�h@eO�@d��@dZ@c��@c�
@c��@c@b�\@b�@a�@a��@aG�@`�`@`�@`Q�@` �@_��@_��@_;d@^�y@^�+@^ff@^$�@]��@]O�@\�@\z�@\I�@\1@[ƨ@[C�@Z�@Z�@Y��@Y��@Yx�@Y%@X�9@X�u@XA�@W�;@W��@V��@Vv�@U�T@U?}@T��@UV@UV@Tz�@T1@S�m@S�
@S��@SdZ@SS�@St�@S��@S��@S�@St�@R�!@R^5@R~�@R�@R�@R-@RJ@QX@P��@P�u@O�@Ol�@O+@N��@N�R@N{@M��@MO�@L��@L(�@K�m@K�
@K��@K�@KC�@J��@Jn�@I�@I��@Ihs@IX@I7L@H�`@HQ�@G�P@G
=@F�+@E�@E?}@EV@D��@D�/@D�j@D9X@C��@CdZ@C"�@B�@B��@B�!@B��@B�\@Bn�@A��@AX@@��@?�@?|�@?�@>��@>�@>�R@>v�@=�-@=V@<��@<(�@<�@;��@;�
@;�
@;�F@;�@;"�@:�H@:��@:��@:�\@:-@9�#@9X@9%@8�`@8�u@81'@7��@7��@7;d@7
=@6��@6ȴ@6E�@6V@6E�@6{@5��@5?}@4j@3�m@3t�@3"�@3@2~�@2^5@2M�@2J@1�#@1��@1��@17L@0Ĝ@0�9@0��@0�u@0�@0A�@0A�@0  @/��@.v�@.@-@-�-@-��@-�h@-�h@-p�@,�@,�j@,�@,��@,�D@,9X@+�
@+C�@*��@*M�@*-@)��@)hs@(��@(Ĝ@(�@(r�@(Q�@(1'@'�@'\)@'
=@&ȴ@&��@&v�@&V@&@%��@%�h@%�@$�@$�D@$j@$Z@$1@#�
@#��@#t�@#33@"�@"��@"M�@!�^@!�7@!7L@!�@ ��@ ��@ 1'@�;@��@K�@�@ȴ@ȴ@�R@��@��@��@��@�+@5?@@�-@�h@`B@V@�@�@�D@z�@j@9X@1@��@ƨ@�@dZ@S�@33@�H@�!@n�@^5@^5@~�@��@��@n�@=q@�@��@��@7L@�u@Q�@b@�;@��@�P@K�@K�@�@�R@�+@v�@{@p�@/@V@��@��@j@(�@1@�
@��@�@�@S�@�@�\@M�@�@��@�#@�#@�^@x�@7L@7L@&�@��@Ĝ@Ĝ@�9@��@�@r�@bN@A�@ �@ �@  @�@�;@��@��@��@l�@�@��@ȴ@�R@��@v�@V@5?@{@��@@��@p�@O�@�@�@�j@�j@�D@j@9X@(�@��@��@�@t�@dZ@S�@33@@
�H@
��@
��@
M�@
J@	��@	�#@	�#@	�7@	hs@	G�@	%@�`@Ĝ@�9@�u@bN@bN@Q�@ �@b@  @��@�@�P@l�@�@��@v�@ff@5?@@�T@��@��@��@�h@�h@p�@`B@?}@�@��@��@��@�D@z�@z�@Z@9X@�@�m@ƨ@�F@t�@o@�H@�\@n�@^5@=q@=q@-@��@��@��@�7@hs@G�@�@ �`@ Ĝ@ �@ A�?��;?���?��?���?�5??�{?��?��-?�p�?�O�?�/?���?��D?��?�"�?�?��H?�~�?�=q?��#?�x�?�x�?�X?��?���?��u?�r�?�Q�?�1'?�b?�b?��?��?�l�?��+?�$�?��T?��TA�$�A�"�A���A�A� �A~�`A|��Ax��Aq;dAiS�Aa��A^E�AZȴAW�^AU�ATbAR��AP�uAN�AM�#AK�AI�hAH��AHAF$�AD�jAC�TAAl�A@ffA?p�A>��A=33A;x�A8�+A4��A3p�A0=qA-��A*=qA'?}A%C�A!hsA�A�At�A�+A �A�AM�A��AVA\)A
�uA
Q�AjAv�A�AK�Ar�A=qA�HAM�AbAA�hA?}A �A ��A (�@�C�@���@�S�@��-@���@��@�{@��w@�{@��T@��@��@��j@�(�@��m@��@�l�@��H@���@�v�@�5?@���@�?}@��@��/@���@�Ĝ@��j@��@�D@�(�@�@�R@�@���@�%@�@�dZ@�ȴ@�@���@@��@�G�@�b@�l�@�^5@�`B@�u@�;d@��y@��@�^@�o@���@��`@���@�C�@�n�@ݙ�@�/@��/@�bN@�\)@��y@ڧ�@�ff@ڗ�@�v�@�@�?}@�9X@�+@�^5@�/@�`B@Լj@�Z@Ӯ@���@�v�@���@�X@љ�@�G�@��@̛�@�bN@��@���@˝�@ɩ�@�V@�Ĝ@�l�@�$�@�t�@Ǿw@�b@��y@�E�@���@���@��@��@���@��@�bN@� �@�1'@�I�@�33@���@�p�@��@���@���@�ƨ@�J@���@���@��@���@�33@��@�\)@�
=@��R@�{@��@��/@��u@�Z@��@�|�@�ȴ@�J@��#@�p�@��@�Z@�(�@�dZ@��#@���@�j@�1'@��;@��@�C�@��+@��-@��@�hs@��@��@��/@�Ĝ@�z�@��
@�dZ@�K�@�33@��H@��R@�V@�@���@�G�@��@���@��`@���@�(�@��@�K�@�o@��@��y@�ff@�-@��@��@���@�`B@�hs@��7@�?}@�G�@�&�@�%@���@���@��D@�bN@��u@�?}@�?}@��/@���@�j@��@��m@���@�dZ@���@���@�n�@���@���@�O�@���@���@�p�@���@�Q�@�ƨ@��R@�5?@�J@���@��@��/@�1'@�  @��m@���@�l�@�;d@�@���@���@�ff@�-@�{@���@�O�@�O�@��@��/@���@���@�1@��F@���@�dZ@�
=@��@���@���@�v�@�ff@�M�@��@��7@�X@�/@��`@���@�Z@�A�@�9X@� �@��P@�l�@�l�@�l�@�C�@�o@��H@��+@�n�@�^5@�E�@���@���@��h@�G�@���@���@�z�@�Q�@�1'@�  @��w@��@���@�K�@��@�@��H@���@���@�v�@�E�@��@���@��#@��-@��@�O�@�V@���@�A�@�b@��
@��P@�|�@�dZ@�K�@�
=@��H@��!@��\@�~�@�V@�J@���@�x�@�O�@���@���@�z�@�(�@��@��F@��@�"�@�@��H@���@�ff@�V@��@��@��T@��^@���@�X@�/@�V@��`@��`@���@���@��D@�bN@�(�@��m@��@��@�\)@��H@���@�v�@�J@��-@���@�x�@�G�@�/@�&�@���@��9@��@�9X@��@��@l�@;d@
=@~��@~V@}��@}�h@}p�@}O�@}�@|��@|�@|��@|z�@|9X@{�
@{"�@zn�@y��@y�@x��@x�9@x�u@x �@w��@w�P@wl�@w\)@w�@v�y@v��@v5?@u�T@u�h@uO�@t�/@tz�@s��@sC�@so@r��@r=q@rJ@q��@q��@qx�@q�@p�`@p�9@pr�@pr�@pbN@pbN@p1'@pb@o��@o�@o\)@o+@nv�@m��@m/@l��@l��@l��@lz�@lZ@l9X@k��@k�@j��@j=q@jJ@i��@h��@hĜ@hr�@h  @g�;@g\)@f�R@fE�@f5?@f@e�-@e�@d��@d�@dj@d1@c��@ct�@co@b��@b~�@bM�@b�@a�#@a�7@a�@`�`@`Ĝ@`��@`r�@_�@_\)@^��@]@\z�@\�@[�m@[��@[�m@["�@Z-@Y�7@YG�@Y7L@X�`@XĜ@Xr�@X1'@W�;@W�@W;d@V�y@Vȴ@V��@V��@VE�@U��@U��@Up�@U`B@UO�@T��@T��@T�@Tz�@TI�@T�@T1@S�m@S�F@SS�@S"�@R��@R=q@RJ@Q��@Q��@QG�@P�`@P�@PQ�@P �@P  @O��@O\)@N�@Nff@N$�@M�@M��@M�h@M?}@L��@L9X@K�m@K�@K33@Ko@K@JM�@I�^@I�7@I7L@H�9@Hr�@H �@G�w@G��@Gl�@G
=@F�@F��@FV@F@E@E�h@E/@EV@D�j@DZ@DZ@D1@C��@Ct�@C"�@B��@BJ@Ahs@A�@@��@@��@@A�@?�;@?�@=�T@=p�@=V@<�@;�F@:�@:M�@:�!@9hs@7�@7��@7�;@8 �@7�@8�9@8Ĝ@8��@8b@6ȴ@6{@6@5�@5�T@5@5p�@5/@4��@4I�@3��@333@2�@2��@2~�@2��@2M�@1�@0�@0A�@0b@0b@/�@/l�@/;d@.�y@.ȴ@.�+@.E�@-��@-/@,��@,z�@,z�@,Z@,1@+�F@+��@+dZ@*��@*^5@*=q@)��@)x�@)7L@)&�@)�@(��@(Ĝ@(�u@(1'@(  @'��@'�P@'K�@'
=@&ȴ@&��@&��@&v�@&V@&5?@%�T@%�-@%/@%V@%V@$�@$�@$j@$I�@$1@#�
@#�F@#�F@#�
@#��@#�F@#t�@#t�@#t�@#t�@#dZ@#S�@#@"�H@"��@"~�@"=q@!��@!�@!�#@!��@!�7@!X@!G�@!%@ �9@ r�@   @|�@;d@�@��@ff@�T@��@�@�/@��@33@��@n�@�@�@�@�^@��@�7@x�@X@&�@��@��@Ĝ@��@�@r�@bN@Q�@A�@b@��@�w@+@ff@�T@��@p�@�@�+@
=@�y@�R@�R@�+@5?@@�h@p�@/@�@�@�j@�D@j@(�@�
@��@dZ@o@��@�!@�\@-@��@�@�^@��@��@x�@G�@��@�9@�9@r�@1'@  @��@��@|�@K�@+@�@
=@��@E�@5?@{@@�T@�-@p�@/@�@�@��@��@�D@z�@Z@I�@9X@1@�
@ƨ@�@S�@C�@33@o@
�@
��@
�\@
~�@
n�@
=q@
-@
�@	��@	�^@	��@	�7@	�7@	X@	&�@�`@�`@Ĝ@�@bN@A�@ �@ �@�@�P@l�@K�@;d@;d@��@�@�R@�R@��@ff@E�@@�-@�h@�h@p�@O�@/@��@�/@�j@��@�D@z�@z�@Z@9X@��@�m@�
@ƨ@��@dZ@o@@�@�H@�!@~�@^5@�@�@�#@��@hs@hs@G�@7L@�@ �`@ ��@ �9@ ��@ �u@ �@ bN@ 1'?��;?�\)?��?��?���?���?�5??�{?��-?�p�?�/?�V?��?��?�j?�(�?��m?�ƨ?�dZ?�?���?���?���?�^5?��#?�x�?�7L?��?���?�r�?��?��P?�
=?���G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111            Am�mAm�mAm�mAm�mAm�mAm�-AlAi�-Ag��Ae�^Ad��A\�AU�-AR��AQ�AP�AO+AM;dAK�AJ��AI�-AH��AG�;AF�+AE�PAEAD1AC�AB��AA��A@�jA?�#A=A=+A<ZA;�A9�A6-A3?}A2=qA/�;A,�DA&�jA#�#A"�!Ax�A��AQ�AdZA�PA  Ap�A�
A;dA	��A�AJA�+A��A�^A�
A�hAt�A33AffA��A�-A��AJA;dA�;A �9@��-@��@��9@�j@��w@���@�S�@��!@�1'@�"�@�l�@���@�?}@��@�1'@��P@�"�@�33@���@�ȴ@�=q@�?}@���@���@�z�@�1'@�|�@���@�@���@�9@�I�@�@���@��@�7L@�1@�w@�\)@�@�O�@�%@�9@�z�@�@���@�+@�=q@�@���@��
@�!@��@�Ĝ@�S�@���@��@�bN@ۅ@��@ڰ!@ڏ\@ف@�V@��#@�7L@�r�@ٺ^@���@ա�@պ^@��@���@ج@�bN@�K�@��@և+@�M�@�{@�&�@�A�@�t�@҇+@�n�@Ѳ-@�`B@�j@·+@��T@��#@�hs@�Ĝ@̋D@��@ɩ�@ʏ\@��y@�hs@���@�x�@ċD@��
@�K�@+@��h@�?}@�1@�;d@�+@��@�Z@��9@���@��@���@���@�V@��R@�+@��@���@�^5@��7@�O�@�7L@���@�bN@���@��@��\@�V@�M�@��@���@���@�dZ@�{@���@���@�|�@�\)@�33@���@��#@��-@��^@���@���@���@�x�@��`@��@�z�@���@��@�o@���@�J@��-@�X@�7L@���@�bN@�9X@��@���@��@�"�@��@�@��@�?}@�`B@�hs@���@�33@�@�@���@��h@�hs@�?}@�7L@�/@���@�r�@� �@��@��m@�\)@�+@�+@��!@�^5@�M�@�-@�@��T@��T@���@���@�hs@�V@�%@�%@�1@���@���@�@���@���@�%@���@�z�@�9X@�z�@���@�Q�@�b@�(�@�1@��w@��P@�|�@��F@�l�@�S�@��@���@���@��\@�J@��h@�O�@�Ĝ@�r�@�r�@�A�@�  @��@�t�@��@�v�@�v�@�ff@��^@�&�@���@�I�@��m@���@���@�K�@��@��@���@�~�@�-@�@�x�@�hs@�O�@�7L@���@�z�@�A�@�  @��
@�dZ@��H@���@�n�@�5?@��T@��^@�p�@�O�@�?}@�?}@��@�Ĝ@���@��D@�j@�1'@��@��;@���@��P@�|�@�S�@��@���@���@�n�@�$�@��@��#@���@�@���@���@���@���@��h@�p�@�G�@�&�@�%@���@���@���@�bN@���@��@��;@���@���@�|�@�l�@�\)@�K�@��@��H@�n�@��@���@�x�@�/@��`@���@��9@��u@�z�@�Q�@�b@���@�ƨ@���@��P@�t�@�C�@�o@���@��y@�ȴ@���@���@�n�@�5?@�{@��@��#@���@��^@��h@�/@�V@��/@���@��@�bN@�9X@�  @�@�P@\)@~��@~5?@}�-@}�@}`B@}�@|z�@|1@{�m@{�
@{ƨ@{�@{o@z�\@z=q@y�^@y�7@yhs@y&�@xĜ@xA�@w�;@w�P@wK�@w
=@v��@v��@v5?@u��@t�j@tI�@t1@s��@sdZ@s33@r��@r^5@q�#@q��@qhs@qX@p�`@p�@o�@o�P@ol�@ol�@o\)@o;d@n�y@nv�@nff@nff@m�T@m��@m`B@m�@l�D@lI�@k��@kƨ@kt�@j�H@j^5@i��@i��@ix�@iX@i�@h�u@hQ�@h �@g�@g�w@g�P@fȴ@f$�@f@f@e�@e@e�h@eO�@d��@dZ@c��@c�
@c��@c@b�\@b�@a�@a��@aG�@`�`@`�@`Q�@` �@_��@_��@_;d@^�y@^�+@^ff@^$�@]��@]O�@\�@\z�@\I�@\1@[ƨ@[C�@Z�@Z�@Y��@Y��@Yx�@Y%@X�9@X�u@XA�@W�;@W��@V��@Vv�@U�T@U?}@T��@UV@UV@Tz�@T1@S�m@S�
@S��@SdZ@SS�@St�@S��@S��@S�@St�@R�!@R^5@R~�@R�@R�@R-@RJ@QX@P��@P�u@O�@Ol�@O+@N��@N�R@N{@M��@MO�@L��@L(�@K�m@K�
@K��@K�@KC�@J��@Jn�@I�@I��@Ihs@IX@I7L@H�`@HQ�@G�P@G
=@F�+@E�@E?}@EV@D��@D�/@D�j@D9X@C��@CdZ@C"�@B�@B��@B�!@B��@B�\@Bn�@A��@AX@@��@?�@?|�@?�@>��@>�@>�R@>v�@=�-@=V@<��@<(�@<�@;��@;�
@;�
@;�F@;�@;"�@:�H@:��@:��@:�\@:-@9�#@9X@9%@8�`@8�u@81'@7��@7��@7;d@7
=@6��@6ȴ@6E�@6V@6E�@6{@5��@5?}@4j@3�m@3t�@3"�@3@2~�@2^5@2M�@2J@1�#@1��@1��@17L@0Ĝ@0�9@0��@0�u@0�@0A�@0A�@0  @/��@.v�@.@-@-�-@-��@-�h@-�h@-p�@,�@,�j@,�@,��@,�D@,9X@+�
@+C�@*��@*M�@*-@)��@)hs@(��@(Ĝ@(�@(r�@(Q�@(1'@'�@'\)@'
=@&ȴ@&��@&v�@&V@&@%��@%�h@%�@$�@$�D@$j@$Z@$1@#�
@#��@#t�@#33@"�@"��@"M�@!�^@!�7@!7L@!�@ ��@ ��@ 1'@�;@��@K�@�@ȴ@ȴ@�R@��@��@��@��@�+@5?@@�-@�h@`B@V@�@�@�D@z�@j@9X@1@��@ƨ@�@dZ@S�@33@�H@�!@n�@^5@^5@~�@��@��@n�@=q@�@��@��@7L@�u@Q�@b@�;@��@�P@K�@K�@�@�R@�+@v�@{@p�@/@V@��@��@j@(�@1@�
@��@�@�@S�@�@�\@M�@�@��@�#@�#@�^@x�@7L@7L@&�@��@Ĝ@Ĝ@�9@��@�@r�@bN@A�@ �@ �@  @�@�;@��@��@��@l�@�@��@ȴ@�R@��@v�@V@5?@{@��@@��@p�@O�@�@�@�j@�j@�D@j@9X@(�@��@��@�@t�@dZ@S�@33@@
�H@
��@
��@
M�@
J@	��@	�#@	�#@	�7@	hs@	G�@	%@�`@Ĝ@�9@�u@bN@bN@Q�@ �@b@  @��@�@�P@l�@�@��@v�@ff@5?@@�T@��@��@��@�h@�h@p�@`B@?}@�@��@��@��@�D@z�@z�@Z@9X@�@�m@ƨ@�F@t�@o@�H@�\@n�@^5@=q@=q@-@��@��@��@�7@hs@G�@�@ �`@ Ĝ@ �@ A�?��;?���?��?���?�5??�{?��?��-?�p�?�O�?�/?���?��D?��?�"�?�?��H?�~�?�=q?��#?�x�?�x�?�X?��?���?��u?�r�?�Q�?�1'?�b?�b?��?��?�l�?��+?�$�?��T?��TA�$�A�"�A���A�A� �A~�`A|��Ax��Aq;dAiS�Aa��A^E�AZȴAW�^AU�ATbAR��AP�uAN�AM�#AK�AI�hAH��AHAF$�AD�jAC�TAAl�A@ffA?p�A>��A=33A;x�A8�+A4��A3p�A0=qA-��A*=qA'?}A%C�A!hsA�A�At�A�+A �A�AM�A��AVA\)A
�uA
Q�AjAv�A�AK�Ar�A=qA�HAM�AbAA�hA?}A �A ��A (�@�C�@���@�S�@��-@���@��@�{@��w@�{@��T@��@��@��j@�(�@��m@��@�l�@��H@���@�v�@�5?@���@�?}@��@��/@���@�Ĝ@��j@��@�D@�(�@�@�R@�@���@�%@�@�dZ@�ȴ@�@���@@��@�G�@�b@�l�@�^5@�`B@�u@�;d@��y@��@�^@�o@���@��`@���@�C�@�n�@ݙ�@�/@��/@�bN@�\)@��y@ڧ�@�ff@ڗ�@�v�@�@�?}@�9X@�+@�^5@�/@�`B@Լj@�Z@Ӯ@���@�v�@���@�X@љ�@�G�@��@̛�@�bN@��@���@˝�@ɩ�@�V@�Ĝ@�l�@�$�@�t�@Ǿw@�b@��y@�E�@���@���@��@��@���@��@�bN@� �@�1'@�I�@�33@���@�p�@��@���@���@�ƨ@�J@���@���@��@���@�33@��@�\)@�
=@��R@�{@��@��/@��u@�Z@��@�|�@�ȴ@�J@��#@�p�@��@�Z@�(�@�dZ@��#@���@�j@�1'@��;@��@�C�@��+@��-@��@�hs@��@��@��/@�Ĝ@�z�@��
@�dZ@�K�@�33@��H@��R@�V@�@���@�G�@��@���@��`@���@�(�@��@�K�@�o@��@��y@�ff@�-@��@��@���@�`B@�hs@��7@�?}@�G�@�&�@�%@���@���@��D@�bN@��u@�?}@�?}@��/@���@�j@��@��m@���@�dZ@���@���@�n�@���@���@�O�@���@���@�p�@���@�Q�@�ƨ@��R@�5?@�J@���@��@��/@�1'@�  @��m@���@�l�@�;d@�@���@���@�ff@�-@�{@���@�O�@�O�@��@��/@���@���@�1@��F@���@�dZ@�
=@��@���@���@�v�@�ff@�M�@��@��7@�X@�/@��`@���@�Z@�A�@�9X@� �@��P@�l�@�l�@�l�@�C�@�o@��H@��+@�n�@�^5@�E�@���@���@��h@�G�@���@���@�z�@�Q�@�1'@�  @��w@��@���@�K�@��@�@��H@���@���@�v�@�E�@��@���@��#@��-@��@�O�@�V@���@�A�@�b@��
@��P@�|�@�dZ@�K�@�
=@��H@��!@��\@�~�@�V@�J@���@�x�@�O�@���@���@�z�@�(�@��@��F@��@�"�@�@��H@���@�ff@�V@��@��@��T@��^@���@�X@�/@�V@��`@��`@���@���@��D@�bN@�(�@��m@��@��@�\)@��H@���@�v�@�J@��-@���@�x�@�G�@�/@�&�@���@��9@��@�9X@��@��@l�@;d@
=@~��@~V@}��@}�h@}p�@}O�@}�@|��@|�@|��@|z�@|9X@{�
@{"�@zn�@y��@y�@x��@x�9@x�u@x �@w��@w�P@wl�@w\)@w�@v�y@v��@v5?@u�T@u�h@uO�@t�/@tz�@s��@sC�@so@r��@r=q@rJ@q��@q��@qx�@q�@p�`@p�9@pr�@pr�@pbN@pbN@p1'@pb@o��@o�@o\)@o+@nv�@m��@m/@l��@l��@l��@lz�@lZ@l9X@k��@k�@j��@j=q@jJ@i��@h��@hĜ@hr�@h  @g�;@g\)@f�R@fE�@f5?@f@e�-@e�@d��@d�@dj@d1@c��@ct�@co@b��@b~�@bM�@b�@a�#@a�7@a�@`�`@`Ĝ@`��@`r�@_�@_\)@^��@]@\z�@\�@[�m@[��@[�m@["�@Z-@Y�7@YG�@Y7L@X�`@XĜ@Xr�@X1'@W�;@W�@W;d@V�y@Vȴ@V��@V��@VE�@U��@U��@Up�@U`B@UO�@T��@T��@T�@Tz�@TI�@T�@T1@S�m@S�F@SS�@S"�@R��@R=q@RJ@Q��@Q��@QG�@P�`@P�@PQ�@P �@P  @O��@O\)@N�@Nff@N$�@M�@M��@M�h@M?}@L��@L9X@K�m@K�@K33@Ko@K@JM�@I�^@I�7@I7L@H�9@Hr�@H �@G�w@G��@Gl�@G
=@F�@F��@FV@F@E@E�h@E/@EV@D�j@DZ@DZ@D1@C��@Ct�@C"�@B��@BJ@Ahs@A�@@��@@��@@A�@?�;@?�@=�T@=p�@=V@<�@;�F@:�@:M�@:�!@9hs@7�@7��@7�;@8 �@7�@8�9@8Ĝ@8��@8b@6ȴ@6{@6@5�@5�T@5@5p�@5/@4��@4I�@3��@333@2�@2��@2~�@2��@2M�@1�@0�@0A�@0b@0b@/�@/l�@/;d@.�y@.ȴ@.�+@.E�@-��@-/@,��@,z�@,z�@,Z@,1@+�F@+��@+dZ@*��@*^5@*=q@)��@)x�@)7L@)&�@)�@(��@(Ĝ@(�u@(1'@(  @'��@'�P@'K�@'
=@&ȴ@&��@&��@&v�@&V@&5?@%�T@%�-@%/@%V@%V@$�@$�@$j@$I�@$1@#�
@#�F@#�F@#�
@#��@#�F@#t�@#t�@#t�@#t�@#dZ@#S�@#@"�H@"��@"~�@"=q@!��@!�@!�#@!��@!�7@!X@!G�@!%@ �9@ r�@   @|�@;d@�@��@ff@�T@��@�@�/@��@33@��@n�@�@�@�@�^@��@�7@x�@X@&�@��@��@Ĝ@��@�@r�@bN@Q�@A�@b@��@�w@+@ff@�T@��@p�@�@�+@
=@�y@�R@�R@�+@5?@@�h@p�@/@�@�@�j@�D@j@(�@�
@��@dZ@o@��@�!@�\@-@��@�@�^@��@��@x�@G�@��@�9@�9@r�@1'@  @��@��@|�@K�@+@�@
=@��@E�@5?@{@@�T@�-@p�@/@�@�@��@��@�D@z�@Z@I�@9X@1@�
@ƨ@�@S�@C�@33@o@
�@
��@
�\@
~�@
n�@
=q@
-@
�@	��@	�^@	��@	�7@	�7@	X@	&�@�`@�`@Ĝ@�@bN@A�@ �@ �@�@�P@l�@K�@;d@;d@��@�@�R@�R@��@ff@E�@@�-@�h@�h@p�@O�@/@��@�/@�j@��@�D@z�@z�@Z@9X@��@�m@�
@ƨ@��@dZ@o@@�@�H@�!@~�@^5@�@�@�#@��@hs@hs@G�@7L@�@ �`@ ��@ �9@ ��@ �u@ �@ bN@ 1'?��;?�\)?��?��?���?���?�5??�{?��-?�p�?�/?�V?��?��?�j?�(�?��m?�ƨ?�dZ?�?���?���?���?�^5?��#?�x�?�7L?��?���?�r�?��?��P?�
=?���G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111            G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�G�O�PRES            TEMP            PSAL            PRES            TEMP            PSAL            PRES_ADJUSTED = PRES - surface_pressure                                                                                                                                                                                                                         none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            PRES_ADJUSTED = PRES - surface_pressure                                                                                                                                                                                                                         none                                                                                                                                                                                                                                                            none                                                                                                                                                                                                                                                            surface_pressure=-0.08 dbar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     surface_pressure=-0.16 dbar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     Pressure adjusted at real time based on most recent valid surface pressure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Pressure adjusted at real time based on most recent valid surface pressure                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      201506161917322015061619173220150616191732201506261918532015062619185320150626191853AO  IF  ARCACORTADJPCOOA    6.2                                                                 RTQCGL01                                                        2015061619173220150628132300IP  QCP$                TEMP            G�O�G�O�G�O�G�O�G�O�G�O�                                AO  AO  ARGQARCAQCPLADJP                                                                                                                                        2015061619173220150626191853QCP$IP                                  G�O�G�O�G�O�G�O�G�O�G�O�0                               AO  AO  ARGQARGQQCPLQCPL                                                                                                                                        2015061619173220150626191853QCF$QCP$                                G�O�G�O�G�O�G�O�G�O�G�O�0               5F03E           IF  AO  CORTARGQCOOAQCPL6.2     RTQCGL01                                                                                                                        2015061911563720150626191853QCP$QCF$TEMP                            G�O�G�O�G�O�G�O�G�O�G�O�                0               IF  IF  CORTCORTCOOACOOA6.2 6.2 RTQCGL01                                                        RTQCGL01                                                        2015061713252020150628132831QCF$QCF$TEMP            PSAL                G�O�B�  G�O�G�O�G�O�6               5               IF  IF  CORT    COOASCOO6.2 1.4 RTQCGL01                                                                                                                        2015061713312320150702112252QCP$QC  PSAL                            G�O�G�O�G�O�G�O�G�O�G�O�                                