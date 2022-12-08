```mermaid
graph TD
    A[Start] -->B{Välj karaktär}
    B --> D[Trollkarl]
    B --> E[Riddaren]
    B --> F[Tjuven]
    D --> G[Välj namn]
    E --> G[Välj namn]
    F --> G[Välj namn]
    G --> H[Äventyr]
    H --> I{Karta}
    I --> J[Liten]
    I --> K[Mellan]
    I --> L[Stor]
    J --> |Rum: 4x4|M{Välj hörn}
    K --> |Rum: 5x5|M{Välj hörn}
    L --> |Rum: 8x8|M{Välj hörn}
    M --> N[Hörn 1]
    M --> O[Hörn 2]
    M --> P[Hörn 3]
    M --> Q[Hörn 4]
    N --> |Riktning| R[N, H]
    O --> |Riktning| S[N, V]
    P --> |Riktning| T[U, H]
    Q --> |Riktning| U[U, V]
    
    
```
