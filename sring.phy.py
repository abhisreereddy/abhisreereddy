public boolean isIsomorphic(String s, String t) {
        String resString1="",resString2="";
            HashMap<Character,Integer> hashmapS = new HashMap(); 
            HashMap<Character,Integer> hashmapT = new HashMap(); 
            boolean flag = false;
            for(int i = 0;i<s.length();i++)
            {
              char chS = s.charAt(i);
              char chT = t.charAt(i);
              if(hashmapS.containsKey(chS))
              {
                  resString1 = resString1 + hashmapS.get(chS);
              }
              else
              {
                  resString1 = resString1 + i; 
                  hashmapS.put(chS, i);
              }
              if(hashmapT.containsKey(chT))
              {
                  resString2 = resString2 + hashmapT.get(chT);
              }
              else
              {
                  resString2 = resString2 + i; 
                  hashmapT.put(chT, i);
              }
            }
           if(resString1.equals(resString2))
               return true;
           else
               return false;
    }
