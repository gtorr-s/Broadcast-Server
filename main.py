import asyncio
import websockets
import argparse

connected_clients = set()

async def handler(websocket):
    connected_clients.add(websocket)
    print(f"Cliente conectado. Total: {len(connected_clients)}")

    try:
        async for message in websocket:
            print(f"Mensagem recebida: {message}")
            await broadcast(f"Mensagem de um cliente: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectado.")
    finally:
        connected_clients.remove(websocket)

async def broadcast(message):
    if connected_clients:
        await asyncio.gather(*[client.send(message) for client in connected_clients])

async def start_server():
    async with websockets.serve(handler, "localhost", 6789):
        print("Servidor iniciado em ws://localhost:6789")
        await asyncio.Future()  # Mantém o servidor rodando

async def start_client():
    try:
        async with websockets.connect("ws://localhost:6789") as websocket:
            print("Conectado ao servidor.")
            print("Digite mensagens para enviar (CTRL+C para sair):")
            while True:
                message = input("> ")
                await websocket.send(message)
                response = await websocket.recv()
                print(f"< {response}")
    except KeyboardInterrupt:
        print("\nCliente encerrado.")
    except Exception as e:
        print(f"Erro ao conectar: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor/Cliente Broadcast")
    parser.add_argument("mode", choices=["start", "connect"], help="start para servidor, connect para cliente")
    args = parser.parse_args()

    if args.mode == "start":
        asyncio.run(start_server())
    elif args.mode == "connect":
        asyncio.run(start_client())
