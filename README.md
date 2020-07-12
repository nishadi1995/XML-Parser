# XML-Parser
- python  
- derive dependencies in a maven project  
- compare two dependency sets of two maven projects  
- under further improvements  

- XML_Paser_1 =>  
    Run 'mvn help:effective-pom -Doutput=result.xml' to generate the effective pom file of the maven project  
    Input two xml files (pom.xml or effective_pom.xml)  
    Derive dependencies from the dependency tag in to two sets  
    compare them to check whether one dependency set is a subset of the other
 
- XML_Paser_2 =>  
    Run 'mvn dependency:tree -DoutputType=txt -DoutputFile=dependency_tree.txt' in the maven project  
    Input dependency_tree.txt file  
    This generates the dependency tree in lists and dictionaries  

- XML_Paser_3 =>   
    Run 'mvn dependency:tree -DoutputType=txt -DoutputFile=dependency_tree.txt' in maven project  
    Input two dependency_tree.txt files  
    Derive dependencies to a set
    Compare them to check whether one dependency set is a subset of the other  
