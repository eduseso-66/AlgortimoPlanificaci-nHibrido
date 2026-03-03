def calculate_metrics(process_list):
    print("\n" + "="*50)
    print(f"{'PROCESO':<15} | {'WAIT':<7} | {'TURNAROUND':<10} | {'TIPO'}")
    print("-" * 50)
    
    total_wait = 0
    
    for p in process_list:
        turnaround = p.completion_time - p.arrival_time
        p.waiting_time = turnaround - p.burst_time
        
        total_wait += p.waiting_time
        
        tipo = "RT" if p.priority < 10 else f"FS ({p.user_id})"
        print(f"{p.name:<15} | {p.waiting_time:<7} | {turnaround:<10} | {tipo}")

    avg_wait = total_wait / len(process_list) if process_list else 0
    print("-" * 50)
    print(f"TIEMPO DE ESPERA PROMEDIO: {avg_wait:.2f}s")
    print("="*50)