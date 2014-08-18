### Description
Pydon scrapes the World Health Organization's Disease Outbreak News reports. Reports can be searched by date only for now, but future versions will allow searching by disease. Pydon outputs lines of the DON text that contain numbers. If there is a table in the DON, there is an option to output the table to .csv. Requirements are Beautiful Soup 4 and pandas.

### Example
'In: text = main('2014_08_', True)`  

```Out:     
2014-08-15  ebola haemhorragic fever
                 New (1)\n Confirmed Probable Suspect Totals
1         Guinea                                            
2          Cases         9       376      133      10    519
3         Deaths         3       245      133       2    380
4        Liberia                                            
5          Cases       116       190      423     173    786
6         Deaths        58       154      190      69    413
7        Nigeria                                            
8          Cases         0        11        0       1     12
9         Deaths         1         4        0       0      4
10  Sierra Leone                                            
11         Cases        27       733       38      39    810
12        Deaths        14       309       34       5    348
13        Totals                                            
14         Cases       152      1310      594     223   2127
15        Deaths        76       712      357      76   1145 

Disease outbreak news
15 August 2014
Between 12 and 13 August 2014, a total of 152 new cases of Ebola virus disease (laboratory-confirmed, probable, and suspect cases) as well as 76 deaths were reported from Guinea, Liberia, Nigeria and Sierra Leone.
On 13-14 August, some airlines and social media and traditional media vehicles expressed concern that air travel to and from affected countries was a high-risk activity for the spread of Ebola
To correct this misunderstanding, WHO called a press conference at the UN Palais des Nations in Geneva on 14 August
On 13 August, Heads of Global Information Systems (GIS) for WHO, UN agencies, intergovernmental agencies, and partners met to continue mapping the EVD crisis and create an interagency common operations picture
© 
        WHO 2014
## End of DON ##
```

Caitlin Rivers    
cmrivers@vbi.vt.edu
