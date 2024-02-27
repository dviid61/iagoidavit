from discord_webhook import DiscordWebhook

def sendMsg(webhook_url, msg):
    webhook = DiscordWebhook(url=webhook_url, content=msg)
    response = webhook.execute()
